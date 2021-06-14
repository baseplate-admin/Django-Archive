const watchMediaQueryFunctionVolume = (event) => {
    if (event.matches) {
        // Mobile Version
        handleSliderInputChange(100)
    } else if (!event.matches) {
        //Desktop Vesion
        handleSliderInputChange(80)
    }
}
// Init the Function Once
watchMediaQueryFunctionVolume(mediaQueryListener)
// Add listener
mediaQueryListener.addListener(watchMediaQueryFunctionVolume)