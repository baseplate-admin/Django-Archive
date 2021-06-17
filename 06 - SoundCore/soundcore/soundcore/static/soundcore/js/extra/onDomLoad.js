const resetValue = () => {
    const transparentSliderInputDiv = document.getElementById('transparent_slider')
    document.getElementById('pause_icon').classList.add('is-hidden')
    transparentSliderInputDiv.value = 0;
}
const setHowlerVolumeToZero = () => {
    // Sets the volume to 0 on load
    Howler.volume(0.00)
}

onDomLoadFunction(setHowlerVolumeToZero)
onDomLoadFunction(resetValue)
