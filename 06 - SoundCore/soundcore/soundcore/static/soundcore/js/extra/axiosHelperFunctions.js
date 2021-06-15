const axiosGetVolumeDataAndMapToVolume = async (url) => {
    const updateVolumeSlider = async (volume) => {
        const setGlobalVolume = async (input) => {
            Howler.volume(input / 100)
        }
        const volumeSliderElement = document.querySelector('.volume_slider')
        const volumeProgressElement = document.querySelector('.volume_progress')

        volumeProgressElement.value = volume
        volumeSliderElement.value = volume

        await setGlobalVolume(volume)
    }

    const res = await axios.get(url)
    // Try..Catch to set the Volume.
    // If theres no user. The volume will be automatically set to 100.
    try {
        const data = JSON.parse(res.data)
        const dataField = _.map(data, 'fields')
        const volumeField = _.map(dataField, "volume")
        await updateVolumeSlider(volumeField)
    } catch (e) {
        await updateVolumeSlider(100)
    }
}
const axiosPostVolumeData = async (url, volume) => {
    const getCookie = async (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = await getCookie('csrftoken');

    const config = {
        headers: {
            'X-CSRFToken': csrftoken
        }
    }
    await axios.post(url, volume, config)
}