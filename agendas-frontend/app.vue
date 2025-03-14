<template>
  <div class="min-h-screen bg-background flex flex-col">
    <header class="border-b sticky top-0 bg-background z-10">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <a href="/" class="flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-6 w-6 text-primary">
              <rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect>
              <line x1="16" x2="16" y1="2" y2="6"></line>
              <line x1="8" x2="8" y1="2" y2="6"></line>
              <line x1="3" x2="21" y1="10" y2="10"></line>
            </svg>
            <h1 class="text-xl font-bold">Sistema de Agendas</h1>
          </a>
          <nav class="flex items-center gap-4">
            <NuxtLink to="/" class="text-sm font-medium hover:underline">
              Dashboard
            </NuxtLink>
            <NuxtLink to="/create" class="text-sm font-medium hover:underline">
              Nova Agenda
            </NuxtLink>
            <a href="https://github.com" target="_blank" class="text-sm font-medium hover:underline flex items-center gap-1">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4">
                <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path>
                <path d="M9 18c-4.51 2-5-2-7-2"></path>
              </svg>
              GitHub
            </a>
          </nav>
        </div>
      </div>
    </header>

    <main class="flex-1">
      <NuxtPage />  <!-- Correctly renders page components -->
    </main>

    <footer class="border-t mt-auto">
      <div class="container mx-auto px-4 py-6">
        <p class="text-center text-sm text-muted-foreground">
          © {{ new Date().getFullYear() }} Sistema de Agendas. Desenvolvido com Vue e Shadcn/UI.
        </p>
      </div>
    </footer>
     <UiToastToaster />

  </div>
</template>

<script setup>
import { Toaster as UiToastToaster } from '@/components/ui/toast'; //  <-- Correct placement: at the top of <script setup>

// No export default {} needed in <script setup> for options API style,
// and definitely not to wrap import statements.
</script>