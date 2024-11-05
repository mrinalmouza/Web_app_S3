async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file first!');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();
        document.getElementById('originalText').textContent = result.text;
    } catch (error) {
        console.error('Error:', error);
        alert('Error uploading file');
    }
}

async function preprocessText() {
    try {
        const response = await fetch('/preprocess', {
            method: 'POST'
        });
        const result = await response.json();
        document.getElementById('processedText').textContent = result.text;
    } catch (error) {
        console.error('Error:', error);
        alert('Error preprocessing text');
    }
}

async function transformText() {
    try {
        const response = await fetch('/transform', {
            method: 'POST'
        });
        const result = await response.json();
        document.getElementById('transformedText').textContent = result.text;
    } catch (error) {
        console.error('Error:', error);
        alert('Error transforming text');
    }
} 