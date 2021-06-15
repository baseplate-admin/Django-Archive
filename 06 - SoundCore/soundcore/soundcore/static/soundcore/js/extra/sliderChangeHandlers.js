const handleSliderInputChange = async () => {
    try {
        const transparentSliderInputDiv = document.getElementById('transparent_slider')
        const sliderProgressBar = document.getElementById('slider_progress')
        sliderProgressBar.value = transparentSliderInputDiv.value
        sound = _.first(howlerArray)
        const duration = (sound.duration() * sliderProgressBar.value) / 100
        sound.seek(duration)
        updateFooterControl()
    } catch (e) {
    }
}
