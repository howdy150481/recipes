import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    outDir: 'static/build', // Pfad zu Ihrem Flask `static` Verzeichnis
    rollupOptions: {
        input: {
            app: resolve(__dirname, 'src/app.js'), // Eingabedatei für JavaScript
            styles: resolve(__dirname, 'src/styles.js'), // Eingabedatei für SCSS
          },
      output: {
        entryFileNames: '[name].js', // Festlegen des Ausgabe-Dateinamens
        chunkFileNames: '[name].js',
        assetFileNames: '[name].[ext]',
      },
    },
  },
  plugins: [], // Fügen Sie hier bei Bedarf Vite-Plugins hinzu
  server: {
    open: false, // Verhindert, dass Vite den Browser beim Start automatisch öffnet
  },
  root: '.', // Setzt das Root-Verzeichnis für Vite auf das Projektverzeichnis
  publicDir: false, // Deaktiviert das öffentliche Verzeichnis, um mögliche Konflikte zu vermeiden
});
