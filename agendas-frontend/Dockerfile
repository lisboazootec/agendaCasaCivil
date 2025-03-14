FROM node:18-slim

WORKDIR /app

# Copia package.json e package-lock.json para aproveitar cache de camadas
COPY package*.json ./

# Instala todas as dependências, incluindo as de desenvolvimento
RUN npm install --legacy-peer-deps

# Copia o resto dos arquivos
COPY . .

# Expõe a porta de desenvolvimento do Nuxt
EXPOSE 3000

# Comando para iniciar o servidor de desenvolvimento
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]