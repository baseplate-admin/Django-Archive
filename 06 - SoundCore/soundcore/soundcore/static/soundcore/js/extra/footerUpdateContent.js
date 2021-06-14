const updateFooterBoilerPlate = async (id) => {
    const previousSongImage = `song-image-${id}`
    const previousSongName = `song-name-${id}`
    const previousSongArtist = `song-artist-${id}`
    const previousSongSampleRate = `song-sample-rate-${id}`

    const previousSongImageDiv = document.getElementById(previousSongImage)
    const previousSongNameDiv = document.getElementById(previousSongName)
    const previousSongArtistDiv = document.getElementById(previousSongArtist)
    const previousSongSampleRateDiv = document.getElementById(previousSongSampleRate)

    const newSongImage = 'footer-song-image'
    const newSongName = 'footer-song-name'
    const newSongArtist = 'footer-song-artist'
    const newSongSampleRate = 'footer-song-sample-rate'

    const newSongImageDiv = document.getElementById(newSongImage)
    const newSongNameDiv = document.getElementById(newSongName)
    const newSongArtistDiv = document.getElementById(newSongArtist)
    const newSongSampleRateDiv = document.getElementById(newSongSampleRate)

    newSongImageDiv.src = previousSongImageDiv.href
    newSongNameDiv.innerText = previousSongNameDiv.innerText
    newSongArtistDiv.innerText = previousSongArtistDiv.innerText
    newSongSampleRateDiv.innerText = `${previousSongSampleRateDiv.innerText} KHz`
}
const updateFooterControl = () => {
    sound = _.first(howlerArray)
    duration = sound.seek();
    const preInputElement = document.querySelector('.pre_input')
    const sliderElement = document.querySelector('#slider_progress')
    const progressElement = document.querySelector('#transparent_slider')
    const convertDurationToHundred = (100 * duration) / sound.duration()

    sliderElement.value = convertDurationToHundred
    progressElement.value = convertDurationToHundred
    preInputElement.innerText = formatTime(duration)
}