onDomLoadFunction(() => {
    // Slider event listener
    document.getElementById('transparent_slider').addEventListener("change", handleSliderInputChange)
    document.getElementById('transparent_slider').addEventListener("input", handleSliderInputChange)
})