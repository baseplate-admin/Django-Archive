const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

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
    const config = {
        headers: {
            'X-CSRFToken': csrftoken
        }
    }
    await axios.post(url, volume, config).catch(e => {
        console.log(`Cant post volume:${volume} to Url:${url}`)
    })
}
const axiosGetRandomSong = async (url) => {
    const config = {
        headers: {
            'X-CSRFToken': csrftoken
        }
    }

    const res = await axios.post(url, {}, config).catch(e => {
        console.log(`Cant get random song from ${url}`)
    })
    await howlerJsPlay((_.first(JSON.parse(res.data)).pk))
}
const axiosPostPreviousSong = async (url, id) => {
    const config = {
        headers: {
            'X-CSRFToken': csrftoken
        }
    }

    await axios.post(url, JSON.stringify({pk: id}), config).catch(e => {
        console.log(`Cant Post Song:${id} to ${url}`)
    })
}
const axiosGetPreviousSong = async (url) => {
    await axios.get(url).then(res => {
        howlerJsPlay((_.first(JSON.parse(res.data)).fields.previous_song))
    }).catch(e => {
        console.log("No Previous Song.")
    })

}