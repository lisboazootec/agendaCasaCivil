<template>
  <div class="bg-gray-100 min-h-screen">
    <div class="container py-8 mx-auto px-4">
      <!-- Header com estatísticas -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <Card class="shadow-lg">
          <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle class="text-sm font-medium text-gray-700">Total de Agendas</CardTitle>
            <Icon name="lucide:calendar" class="h-5 w-5 text-gray-500" />
          </CardHeader>
          <CardContent>
            <div class="text-3xl font-bold text-gray-900">{{ totalAgendas }}</div>
            <p class="text-xs text-gray-500 mt-1">Agendas no sistema</p>
          </CardContent>
        </Card>

        <Card class="shadow-lg">
          <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle class="text-sm font-medium text-gray-700">
              Agendas Confirmadas
            </CardTitle>
            <Icon name="lucide:check-circle" class="h-5 w-5 text-green-500" />
          </CardHeader>
          <CardContent>
            <div class="text-3xl font-bold text-gray-900">{{ confirmedAgendas }}</div>
            <p class="text-xs text-gray-500 mt-1">
              {{ Math.round((confirmedAgendas / (totalAgendas || 1)) * 100) || 0 }}%
              do total
            </p>
          </CardContent>
        </Card>

        <Card class="shadow-lg">
          <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle class="text-sm font-medium text-gray-700">Próxima Agenda</CardTitle>
            <Icon name="lucide:clock" class="h-5 w-5 text-gray-500" />
          </CardHeader>
          <CardContent>
            <div v-if="nextAgenda" class="text-xl font-bold text-gray-900">
              {{ formatDate(nextAgenda.dataInicio) }}
            </div>
            <div v-else class="text-xl font-bold text-gray-900">-</div>
            <p v-if="nextAgenda" class="text-xs text-gray-500 mt-1">
              {{ nextAgenda.titulo }}
            </p>
            <p v-else class="text-xs text-gray-500 mt-1">
              Nenhuma agenda próxima
            </p>
          </CardContent>
        </Card>
      </div>

      <!-- Tabela de Agendas -->
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-3xl font-bold tracking-tight text-gray-900">Agendas</h2>
        <Button @click="navigateTo('/create')" class="bg-blue-500 hover:bg-blue-600 text-white">
          <Icon name="lucide:plus" class="mr-2 h-4 w-4" />
          Nova Agenda
        </Button>
      </div>

      <Card class="shadow-lg">
        <CardContent class="pt-6">
          <div v-if="loading" class="flex justify-center p-8">
            <Icon name="lucide:loader-2" class="h-8 w-8 animate-spin text-blue-500" />
          </div>

          <div
            v-else-if="agendas.length === 0"
            class="flex flex-col items-center justify-center p-8 text-center"
          >
            <Icon name="lucide:calendar-off" class="h-10 w-10 text-gray-400 mb-4" />
            <h3 class="text-lg font-medium text-gray-700">Nenhuma agenda encontrada</h3>
            <p class="text-sm text-gray-500 mt-1 mb-4">
              Crie sua primeira agenda para começar a organizar seus eventos.
            </p>
            <Button @click="navigateTo('/create')" class="bg-blue-500 hover:bg-blue-600 text-white">Criar Agenda</Button>
          </div>

          <Table v-else class="border-collapse">
            <TableHeader>
              <TableRow>
                <TableHead class="text-left text-gray-700">Título</TableHead>
                <TableHead class="text-left text-gray-700">Data</TableHead>
                <TableHead class="text-left text-gray-700">Horário</TableHead>
                <TableHead class="text-left text-gray-700">Local</TableHead>
                <TableHead class="text-left text-gray-700">Status</TableHead>
                <TableHead class="text-right text-gray-700">Ações</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow v-for="agenda in agendas" :key="agenda.id" class="hover:bg-gray-50 transition">
                <TableCell class="font-medium text-gray-900">{{ agenda.titulo }}</TableCell>
                <TableCell class="text-gray-700">{{ formatDate(agenda.dataInicio) }}</TableCell>
                <TableCell class="text-gray-700">
                  {{ formatTime(agenda.dataInicio) }} -
                  {{ formatTime(agenda.dataFim) }}
                </TableCell>
                <TableCell class="text-gray-700">{{ agenda.local || "-" }}</TableCell>
                <TableCell>
                  <span
                    class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                    :class="{
                      'bg-yellow-100 text-yellow-800':
                        agenda.estadoAtualAgenda === 'RECEBIDO',
                      'bg-green-100 text-green-800':
                        agenda.estadoAtualAgenda === 'CONFIRMADO',
                      'bg-red-100 text-red-800':
                        agenda.estadoAtualAgenda === 'CANCELADO',
                    }"
                  >
                    {{ getStatusLabel(agenda.estadoAtualAgenda) }}
                  </span>
                </TableCell>
                <TableCell class="text-right">
                  <div class="flex items-center justify-end space-x-2">
                    <Button
                      variant="outline"
                      size="sm"
                      @click="navigateTo(`/edit/${agenda.id}`)"
                      class="hover:bg-gray-200"
                    >
                      <Icon name="lucide:pencil" class="h-4 w-4 text-gray-600" />
                    </Button>
                    <Button
                      variant="outline"
                      size="sm"
                      @click="showDeleteDialog(agenda)"
                      class="hover:bg-gray-200"
                    >
                      <Icon name="lucide:trash" class="h-4 w-4 text-red-600" />
                    </Button>
                  </div>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>

          <!-- Paginação -->
          <div v-if="agendas.length > 0" class="flex justify-end pt-4">
            <Button
              variant="outline"
              size="sm"
              :disabled="!previousPage"
              @click="fetchPage(previousPage)"
              class="hover:bg-gray-200"
            >
              <Icon name="lucide:chevron-left" class="h-4 w-4 text-gray-600" />
            </Button>
            <span class="mx-4 flex items-center text-sm text-gray-700">
              Página {{ currentPage }} de {{ totalPages }}
            </span>
            <Button
              variant="outline"
              size="sm"
              :disabled="!nextPage"
              @click="fetchPage(nextPage)"
              class="hover:bg-gray-200"
            >
              <Icon name="lucide:chevron-right" class="h-4 w-4 text-gray-600" />
            </Button>
          </div>
        </CardContent>
      </Card>

      <!-- Dialog de confirmação de exclusão -->
      <Dialog v-model:open="isDeleteDialogOpen">
        <DialogContent class="sm:max-w-md">
          <DialogHeader>
            <DialogTitle class="text-gray-900">Confirmar exclusão</DialogTitle>
            <DialogDescription class="text-gray-700">
              Tem certeza que deseja excluir a agenda "{{ selectedAgenda?.titulo
              }}"? Esta ação não pode ser desfeita.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter class="flex flex-row-reverse space-x-2 space-x-reverse">
              <Button
                variant="destructive"
                @click="confirmDelete"
                :disabled="deleteLoading"
                class="bg-red-500 hover:bg-red-600 text-white"
              >
                <Icon
                  v-if="deleteLoading"
                  name="lucide:loader-2"
                  class="mr-2 h-4 w-4 animate-spin"
                />
                Excluir
              </Button>
            <Button variant="outline" @click="isDeleteDialogOpen = false" class="bg-gray-200 hover:bg-gray-300">Cancelar</Button>

          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Agenda } from '~/types/agenda'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { useToast } from '@/components/ui/toast/use-toast'
import { useAgendaApi } from '~/composables/useApi'
import { format, parseISO, parse } from 'date-fns'; // Import parseISO and parse
import { useRouter } from 'vue-router';


const router = useRouter(); // Use useRouter for navigation
const { toast } = useToast()
const { getAgendas, deleteAgenda } = useAgendaApi()

// Estado
const agendas = ref<Agenda[]>([])
const totalAgendas = ref(0)
const confirmedAgendas = ref(0)
const nextAgenda = ref<Agenda | null>(null)
const loading = ref(true)
const isDeleteDialogOpen = ref(false)
const selectedAgenda = ref<Agenda | null>(null)
const deleteLoading = ref(false)

// Paginação
const nextPage = ref<string | null>(null)
const previousPage = ref<string | null>(null)
const currentPage = ref(1)
const totalPages = ref(1)

onMounted(async () => {
  await fetchAgendas()
})

const fetchAgendas = async () => {
  loading.value = true;
  try {
    const response = await getAgendas();

    if (response && response.results && Array.isArray(response.results)) {
      agendas.value = response.results;
      totalAgendas.value = response.count || 0;
      confirmedAgendas.value = agendas.value.filter(
        (a) => a.estadoAtualAgenda === 'CONFIRMADO'
      ).length;
      nextPage.value = response.next;
      previousPage.value = response.previous;

      if (response.count) {
        totalPages.value = Math.ceil(response.count / 10);
      }

      // Função para analisar data independente do formato
      const parseDate = (dateString: string) => {
        try {
          // Tenta parseISO primeiro (formato padrão)
          const date = parseISO(dateString);
          
          // Verifica se a data é válida
          if (!isNaN(date.getTime())) {
            return date;
          }
          
          // Se parseISO falhar, tenta outros formatos comuns
          // Esta parte é um fallback caso suas datas estejam em formato diferente
          const formats = [
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ss.SSS",
            "yyyy-MM-dd'T'HH:mm:ss",
            "yyyy-MM-dd HH:mm:ss.SSSSSS",
            "yyyy-MM-dd HH:mm:ss",
            "yyyy-MM-dd"
          ];
          
          for (const formatStr of formats) {
            try {
              const parsedDate = parse(dateString, formatStr, new Date());
              if (!isNaN(parsedDate.getTime())) {
                return parsedDate;
              }
            } catch (e) {
              // Continua tentando outros formatos
            }
          }
          
          // Se tudo falhar, tenta o construtor Date como último recurso
          const fallbackDate = new Date(dateString);
          if (!isNaN(fallbackDate.getTime())) {
            return fallbackDate;
          }
          
          throw new Error(`Não foi possível analisar a data: ${dateString}`);
        } catch (error) {
          console.error(`Erro ao analisar data: ${dateString}`, error);
          return null;
        }
      };

      const now = new Date();
      
      // Filtra agendas futuras não canceladas
      const futureAgendas = agendas.value
        .filter(agenda => {
          if (agenda.estadoAtualAgenda === 'CANCELADO') return false;
          
          // Usa a função parseDate que é mais robusta
          const agendaDate = parseDate(agenda.dataInicio);
          
          // Verifica se a data é válida e no futuro
          return agendaDate !== null && agendaDate >= now;
        })
        .sort((a, b) => {
          const dateA = parseDate(a.dataInicio) || new Date(0);
          const dateB = parseDate(b.dataInicio) || new Date(0);
          return dateA.getTime() - dateB.getTime();
        });
      
      nextAgenda.value = futureAgendas.length > 0 ? futureAgendas[0] : null;
      
      // Log para debugging
      console.log('Próxima agenda:', nextAgenda.value ? {
        id: nextAgenda.value.id,
        titulo: nextAgenda.value.titulo,
        data: nextAgenda.value.dataInicio,
        dataFormatada: nextAgenda.value.dataInicio ? format(parseDate(nextAgenda.value.dataInicio) || new Date(), 'dd/MM/yyyy HH:mm') : null,
        status: nextAgenda.value.estadoAtualAgenda
      } : 'Nenhuma agenda futura encontrada');
      
    } else if (response.error) {
      toast({
        title: 'Erro',
        description: response.error,
        variant: 'destructive',
      });
    } else {
      toast({
        title: 'Erro',
        description: 'Resposta da API em formato inesperado.',
        variant: 'destructive',
      });
    }
  } catch (error) {
    console.error('Erro ao buscar agendas:', error);
    toast({
      title: 'Erro',
      description: 'Não foi possível carregar as agendas',
      variant: 'destructive',
    });
  } finally {
    loading.value = false;
  }
};

// Função para buscar uma página específica
const fetchPage = async (url: string | null) => {
  if (!url) return

  loading.value = true

  try {
    // Extrair o número da página da URL
    const urlObj = new URL(url)
    const page = urlObj.searchParams.get('page')
    if (page) {
      currentPage.value = parseInt(page, 10) // Specify radix 10
    }

    const response = await fetch(url)
    if (!response.ok) {
      throw new Error('Erro ao buscar página')
    }

    const data = await response.json()
      if (data && data.results && Array.isArray(data.results)) {
        agendas.value = data.results;
        nextPage.value = data.next;
        previousPage.value = data.previous;
      }
       else if (data.error){
        // Handle API errors
        toast({
          title: 'Erro',
          description: data.error,
          variant: 'destructive',
        });
    }
      else {
        toast({
          title: 'Erro',
          description: 'Resposta da API em formato inesperado.',
          variant: 'destructive',
        });
      }

  } catch (error) {
    console.error('Erro ao buscar página:', error)
    toast({
      title: 'Erro',
      description: 'Não foi possível carregar a página',
      variant: 'destructive',
    })
  } finally {
    loading.value = false
  }
}
// *** KEY CHANGE: Use parseISO ***
const formatDate = (dateString: string): string => {
  try {
    const date = parseISO(dateString); // Correctly parse the ISO string
    return format(date, 'dd/MM/yyyy');
  } catch (error) {
    console.error("Erro ao formatar data:", error);
    return "Data inválida";
  }
};

// *** KEY CHANGE: Use parseISO ***
const formatTime = (dateString: string): string => {
  try {
    const date = parseISO(dateString); // Correctly parse the ISO string
    return format(date, 'HH:mm');
  } catch (error) {
    console.error("Erro ao formatar hora:", error);
    return "--:--";
  }
};

const getStatusLabel = (status: string): string => {
  const statusMap: Record<string, string> = {
    RECEBIDO: 'Recebido',
    CONFIRMADO: 'Confirmado',
    CANCELADO: 'Cancelado',
  }
  return statusMap[status] || status
}

const showDeleteDialog = (agenda: Agenda) => {
  selectedAgenda.value = agenda
  isDeleteDialogOpen.value = true
}

const confirmDelete = async () => {
  if (!selectedAgenda.value) return

  deleteLoading.value = true

  try {
    const result = await deleteAgenda(selectedAgenda.value.id) //deleteAgenda returns void
     if (result.error) {
        toast({
            title: 'Erro',
            description: result.error,
            variant: 'destructive'
        });
    } else {
        toast({
          title: 'Agenda excluída',
          description: 'A agenda foi excluída com sucesso',
        })
        await fetchAgendas()
        isDeleteDialogOpen.value = false
        selectedAgenda.value = null
    }

  } catch (error: any) { //melhor prática para error handling com typescript.
    console.error('Erro ao excluir agenda:', error)
        let errorMessage = 'Não foi possível excluir a agenda.';
        if (error && error.message) { // Check if error has a message property
          errorMessage = error.message;
        }
    toast({
      title: 'Erro',
      description: errorMessage,
      variant: 'destructive',
    })
  } finally {
    deleteLoading.value = false
  }
}

// Use vue-router for navigation
const navigateTo = (path: string) => {
  router.push(path);
};
</script>