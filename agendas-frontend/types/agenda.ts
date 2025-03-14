// Interface da Agenda (conforme retornado pela API)
export interface Agenda {
  id: number;
  titulo: string;
  descricao: string;
  dataInicio: string;
  dataFim: string;
  local: string;
  estadoAtualAgenda: 'RECEBIDO' | 'CONFIRMADO' | 'CANCELADO' | 'ATENDIDO';
  created_at: string;
  updated_at: string;
}

// Interface para o formulário no componente Vue
export interface AgendaFormData {
  // Note que aqui estamos usando os nomes dos campos conforme aparecem no seu componente Vue
  title: string;               // Corresponde a titulo na API
  description: string;         // Corresponde a descricao na API
  date: string;                // Será usado para construir dataInicio
  start_time: string;          // Será combinado com date para formar dataInicio
  end_time: string;            // Será combinado com date para formar dataFim
  location: string;            // Corresponde a local na API
  status: 'RECEBIDO' | 'CONFIRMADO' | 'CANCELADO' | 'ATENDIDO';  // Corresponde a estadoAtualAgenda na API
}

// Interface de resposta da API
export interface ApiResponse<T> {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results?: T[];
  data?: T | null;
  error?: string | null;
}

// Interface para mapear da forma do formulário para o formato da API
export interface AgendaApiSubmitData {
  titulo: string;
  descricao: string;
  dataInicio: string;
  dataFim: string;
  local: string;
  estadoAtualAgenda: 'RECEBIDO' | 'CONFIRMADO' | 'CANCELADO' | 'ATENDIDO';
}