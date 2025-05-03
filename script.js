document.addEventListener("DOMContentLoaded", () => {
    const instansiContainer = document.getElementById("instansi-container");
    const jsonFilePath = "data.json"; // Path ke file JSON

    // Fungsi untuk mengambil data JSON
    const fetchInstansiData = async () => {
        try {
            const response = await fetch(jsonFilePath);
            if (!response.ok) {
                throw new Error(`Gagal memuat data JSON: ${response.statusText}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error(error);
            return [];
        }
    };

    // Fungsi untuk menampilkan daftar instansi
    const displayInstansi = (data) => {
        data.forEach((item) => {
            const instansiName = Object.keys(item.instansi)[0];
            const instansiElement = document.createElement("div");
            instansiElement.className = "instansi-item";
            instansiElement.textContent = instansiName;
            instansiContainer.appendChild(instansiElement);
        });
    };

    // Load data dan tampilkan di halaman
    const init = async () => {
        const data = await fetchInstansiData();
        displayInstansi(data);
    };

    init();
});