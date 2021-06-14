const handleSliderInputChange = async () => {
    try {
        const transparentSliderInputDiv = document.getElementById('transparent_slider')
        const sliderProgressBar = document.getElementById('slider_progress')
        sliderProgressBar.value = transparentSliderInputDiv.value
        sound = _.first(howlerArray)
        const duration = (sound.duration() * sliderProgressBar.value) / 100
        sound.seek(duration)
        updateFooterControl()
    }
    catch (e) {
    }
}
const handleVolumeInputChange = (value) => {
    const setGlobalVolume = (input) => {
        Howler.volume(input / 100)
    }

    const volumeProgressElement = document.querySelector('.volume_progress')
    const volume = value
    volumeProgressElement.value = volume
    setGlobalVolume(volume)
}