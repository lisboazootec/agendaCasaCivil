import { useToast } from '@/components/ui/toast/use-toast'

export function useToaster() {
  const { toast } = useToast()

  const success = (title: string, description?: string) => {
    toast({
      title,
      description,
      variant: 'default', // Use 'success' se você implementar a Opção 3
      duration: 3000,
    })
  }

  const error = (title: string, description?: string) => {
    toast({
      title,
      description,
      variant: 'destructive',
      duration: 5000,
    })
  }

  const warning = (title: string, description?: string) => {
    toast({
      title,
      description,
      variant: 'default', // Use 'warning' se você implementar a Opção 3
      duration: 4000,
    })
  }

  const info = (title: string, description?: string) => {
    toast({
      title,
      description,
      variant: 'default', // Use 'info' se você implementar a Opção 3
      duration: 3000,
    })
  }

  return {
    success,
    error,
    warning,
    info
  }
}