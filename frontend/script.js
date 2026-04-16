// Referencias a los elementos de la pantalla
const browseBtn = document.getElementById('browseBtn');
const audioInput = document.getElementById('audioInput');
const loadingText = document.getElementById('loadingText');
const textoOriginalDiv = document.getElementById('textoOriginal');
const textoEncriptadoDiv = document.getElementById('textoEncriptado');

// Cuando le damos clic al botón azul, hacemos que se abra el buscador de archivos oculto
browseBtn.addEventListener('click', () => {
    audioInput.click();
});

// Cuando el usuario selecciona un archivo de audio
audioInput.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    
    if (!file) return;

    // 1. Mostrar mensaje de carga
    loadingText.classList.remove('hidden');
    textoOriginalDiv.innerText = "Procesando...";
    textoEncriptadoDiv.innerText = "Procesando...";

    // 2. Empacar el archivo para enviarlo al backend
    const formData = new FormData();
    formData.append('audio', file);

    try {
        // 3. ¡El disparo! Enviamos el audio a la IA de Python
        const response = await fetch('http://127.0.0.1:8000/procesar-audio', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            // 4. Si todo salió bien, ponemos los resultados en las cajas
            textoOriginalDiv.innerText = data.texto_original;
            textoEncriptadoDiv.innerText = data.texto_encriptado;
        } else {
            // Manejo de errores
            textoOriginalDiv.innerText = "Hubo un error al procesar el audio.";
            textoEncriptadoDiv.innerText = "Error.";
            console.error(data);
        }

    } catch (error) {
        console.error("Error de conexión:", error);
        textoOriginalDiv.innerText = "Error de red. ¿El servidor Backend está encendido?";
        textoEncriptadoDiv.innerText = "";
    } finally {
        // 5. Ocultar el mensaje de carga al terminar
        loadingText.classList.add('hidden');
        // Limpiamos el input por si quiere subir el mismo audio otra vez
        audioInput.value = ''; 
    }
});