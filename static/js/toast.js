function showToast(title, message, type = "info", duration = 3000) {
    const toast = document.getElementById("toast-container");
    const toastTitle = document.getElementById("toast-title");
    const toastMessage = document.getElementById("toast-message");
    const toastIcon = document.getElementById("toast-icon");

    if (!toast) return;

    // Reset style dan ikon
    toast.className =
        "fixed top-6 right-6 max-w-sm w-auto flex items-center gap-3 px-5 py-4 rounded-lg shadow-lg border transition-all duration-300 opacity-0 -translate-y-10 z-50";

    let bgColor = "bg-white";
    let borderColor = "border-gray-300";
    let textColor = "text-gray-800";
    let icon = "ℹ️";

    if (type === "success") {
        bgColor = "bg-green-50";
        borderColor = "border-green-400";
        textColor = "text-green-700";
        icon = "✅";
    } else if (type === "error") {
        bgColor = "bg-red-50";
        borderColor = "border-red-400";
        textColor = "text-red-700";
        icon = "❌";
    } else if (type === "warning") {
        bgColor = "bg-yellow-50";
        borderColor = "border-yellow-400";
        textColor = "text-yellow-700";
        icon = "⚠️";
    }

    // Set tampilan baru
    toast.classList.add(bgColor, borderColor, textColor);
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastIcon.textContent = icon;

    // Animasi muncul
    toast.classList.remove("opacity-0", "-translate-y-10");
    toast.classList.add("opacity-100", "translate-y-0");

    // Hilang otomatis setelah durasi tertentu
    setTimeout(() => {
        toast.classList.remove("opacity-100", "translate-y-0");
        toast.classList.add("opacity-0", "-translate-y-10");
    }, duration);
}
