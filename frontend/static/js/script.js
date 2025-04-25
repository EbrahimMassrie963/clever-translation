document.getElementById("translationForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent the page from reloading on form submission

    const inputText = document.getElementById("input_text").value;
    const targetLanguages = document.getElementById("target_languages").value;

    const requestData = {
        input_text: inputText,
        target_languages: targetLanguages
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        });

        const result = await response.json();

        if (response.status === 200) {
            document.getElementById("translations").innerHTML = `
                <strong>Message:</strong> ${result.message}<br><br>
                <strong>Translations:</strong><br>
                ${Object.entries(result.translations).map(([lang, translation]) => `
                    <strong>${lang}:</strong> ${translation}<br>
                `).join('')}
            `;
        } else {
            document.getElementById("translations").innerHTML = `
                <strong>Error:</strong> ${result.detail}
            `;
        }
    } catch (error) {
        document.getElementById("translations").innerHTML = `
            <strong>Error:</strong> ${error.message}
        `;
    }
});
