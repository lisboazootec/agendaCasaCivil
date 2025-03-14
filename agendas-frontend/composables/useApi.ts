// composables/useApi.ts
import { ref } from 'vue'
import type { Agenda, AgendaFormData, ApiResponse, AgendaApiSubmitData } from '~/types/agenda'

export function useAgendaApi() {
  const config = useRuntimeConfig()
  const baseUrl = config.public.apiBase
  const loading = ref(false)

  const getAgendas = async (): Promise<ApiResponse<Agenda[]>> => { 
    loading.value = true
    try {
      const response = await fetch(`${baseUrl}/agendas/`)
      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Falha ao buscar agendas')
      }
      return await response.json() as Promise<ApiResponse<Agenda[]>>; // Corrected type cast
    } catch (error) {
      console.error('Erro ao buscar agendas:', error)
      const errorMessage = error instanceof Error ? error.message : 'Falha ao buscar agendas'
      return { error: errorMessage }
    } finally {
      loading.value = false
    }
  }

  const getAgenda = async (id: number | string): Promise<ApiResponse<Agenda>> => {
    loading.value = true;
    try {
        const agendaId = typeof id === 'string' ? parseInt(id, 10) : id;
        if (isNaN(agendaId)) {
            throw new Error('ID da agenda inválido.');
        }
        console.log("Calling API with URL:", `${baseUrl}/agendas/${agendaId}/`);
        console.log("Base URL:", baseUrl);

        const response = await fetch(`${baseUrl}/agendas/${agendaId}/`);
        console.log("Raw API response:", response);

        if (!response.ok) {
            const errorData = await response.json();
            console.error("API Error Response:", errorData);
            throw new Error(errorData.detail || `Falha ao buscar a agenda ${agendaId}`);
        }
        
        const jsonData = await response.json();
        console.log("Parsed JSON response:", jsonData);
        
        // Retornando no formato que o componente espera
        return { data: jsonData, error: null };
    } catch (error) {
        console.error(`Erro ao buscar agenda:`, error);
        const errorMessage = error instanceof Error ? error.message : 'Falha ao buscar a agenda';
        return { data: null, error: errorMessage };
    } finally {
        loading.value = false;
    }
}


  const createAgenda = async (data: AgendaFormData): Promise<ApiResponse<Agenda>> => { //Corrected return type
    loading.value = true
    try {
      const response = await fetch(`${baseUrl}/agendas/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        const errorData = await response.json()
         let errorMessage = 'Falha ao criar agenda';
              if (errorData.detail) {
                errorMessage = errorData.detail;
              } else if (typeof errorData === 'object') {
                for (const key in errorData) {
                  if (Array.isArray(errorData[key]) && errorData[key].length > 0) {
                    errorMessage = errorData[key][0];
                    break;
                  }
                }
              }
        throw new Error(errorMessage)
      }

      return await response.json() as Promise<ApiResponse<Agenda>>; // Corrected type cast
    } catch (error) {
      console.error('Erro ao criar agenda:', error)
      const errorMessage = error instanceof Error ? error.message : 'Falha ao criar agenda'
       return { error: errorMessage }
    } finally {
      loading.value = false
    }
  }

  const updateAgenda = async (id: number | string, formData: AgendaApiSubmitData): Promise<ApiResponse<Agenda>> => {
    loading.value = true;
    
    try {
      const agendaId = typeof id === 'string' ? parseInt(id, 10) : id;
      if (isNaN(agendaId)) {
        throw new Error('ID da agenda inválido.');
      }
      
      console.log("Enviando dados para a API:", `${baseUrl}/agendas/${agendaId}/`);
      console.log("Dados a serem enviados:", formData);
      
      const response = await fetch(`${baseUrl}/agendas/${agendaId}/`, {
        method: 'PUT', // ou 'PATCH' se a API esperar um PATCH
        headers: {
          'Content-Type': 'application/json',
          // Adicione headers de autenticação se necessários
        },
        body: JSON.stringify(formData)
      });
      
      console.log("Resposta bruta da API:", response);
      
      if (!response.ok) {
        const errorData = await response.json();
        console.error("Erro na resposta da API:", errorData);
        throw new Error(errorData.detail || `Falha ao atualizar a agenda ${agendaId}`);
      }
      
      const jsonData = await response.json();
      console.log("Resposta JSON parseada:", jsonData);
      
      return { data: jsonData, error: null };
    } catch (error) {
      console.error(`Erro ao atualizar agenda:`, error);
      const errorMessage = error instanceof Error ? error.message : 'Falha ao atualizar a agenda';
      return { data: null, error: errorMessage };
    } finally {
      loading.value = false;
    }
  };

  const deleteAgenda = async (id: number | string): Promise<ApiResponse<null>> => { //Corrected return type
    loading.value = true;
    try {
        const agendaId = typeof id === 'string' ? parseInt(id, 10) : id;
        if (isNaN(agendaId)) {
          throw new Error('ID da agenda inválido.')
        }
      const response = await fetch(`${baseUrl}/agendas/${agendaId}/`, {
        method: 'DELETE',
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Falha ao excluir agenda')
      }

      return { data: null }
    } catch (error) {
      console.error(`Erro ao excluir agenda:`, error)
      const errorMessage = error instanceof Error ? error.message : 'Falha ao excluir agenda'
      return { error: errorMessage }
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    getAgendas,
    getAgenda,
    createAgenda,
    updateAgenda,
    deleteAgenda,
  }
}