import './slider.css'
import './footer.css'
import { useEffect,   useState } from 'react'
import BackwardTenSecondsIcon from './Icons/BackwardTenSeconds'
import ForwardTenSecondsIcon from './Icons/ForwardTenSeconds'
import NextIcon from './Icons/Next'
import PauseIcon from './Icons/Pause'
import PlayIcon from './Icons/Play'
import PreviousIcon from './Icons/Previous'
import { VolumeHighIcon, VolumeLowIcon, VolumeMediumIcon, VolumeMuteIcon, VolumeOffIcon } from './Icons/Volume'
import Fullplayer from './FullPlayer'
export default function MusicFooter(props:any) {
    let color = '#007CC7'

    const [volumeValue, setVolumeValue] = useState(25)

    const [changePlaybackValue, setChangePlaybackValue] = useState(false)


    // Player Control
    const [playDuration, setPlayDuration] = useState(0);
    const [totalPlayDuration, setTotalPlayDuration] = useState(0);
    // Every thing down here is for volume control

    const [showHighVolume,setShowHighVolume] = useState(false);
    const [showMediumVolume, setShowMediumVolume] = useState(false);
    const [showLowVolume, setShowLowVolume] = useState(false);
    const [showVolumeOff, setShowVolumeOff] = useState(false);
    const [showMute, setShowMute] = useState(false);

    const showHighFunc = () =>{
        setShowHighVolume(true)
        setShowMediumVolume(false)
        setShowLowVolume(false)
        setShowVolumeOff(false)
        setShowMute(false)
    }
    const showMediumFunc = () =>{
        setShowHighVolume(false)
        setShowMediumVolume(true)
        setShowLowVolume(false)
        setShowVolumeOff(false)
        setShowMute(false)
    }
    const showLowFunc = () =>{
        setShowHighVolume(false)
        setShowMediumVolume(false)
        setShowLowVolume(true)
        setShowVolumeOff(false)
        setShowMute(false)
    }
    const showVolOffFunc = () =>{
        setShowHighVolume(false)
        setShowMediumVolume(false)
        setShowLowVolume(false)
        setShowVolumeOff(true)
        setShowMute(false)
    }
    const showMuteFunc = () =>{
        setShowHighVolume(false)
        setShowMediumVolume(false)
        setShowLowVolume(false)
        setShowVolumeOff(false)
        setShowMute(true)
    }

    const formatTime = (duration:any) =>
    {   
        // Hours, minutes and seconds
        let hrs = ~~(duration / 3600);
        let mins = ~~((duration % 3600) / 60);
        let secs = ~~duration % 60;
    
        // Output like "1:01" or "4:03:59" or "123:03:59"
        let ret = "";
    
        if (hrs > 0) {
            ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
        }
    
        ret += "" + mins + ":" + (secs < 10 ? "0" : "");
        ret += "" + secs;
        return ret;
    }
    useEffect(()=>{
        if(volumeValue>75 && volumeValue < 100){
            showHighFunc()
        }
        else if(volumeValue > 50 && volumeValue <=75 ){
            showMediumFunc()
        }
        else if (volumeValue >25 && volumeValue <=50) {
            showLowFunc()
        }
        else if (volumeValue > 0 && volumeValue <=25){
            showVolOffFunc()
        }
        else if (volumeValue === 0) {
            showMuteFunc()
        }
            
    },[volumeValue])

    const handleTenSecondsForward = () =>{
        let currentPlayBackValue = playDuration + 10;
        setPlayDuration(currentPlayBackValue )
    }
    const handleTenSecondsBackward =() =>{
        let currentPlayBackValue = playDuration - 10;
        setPlayDuration(currentPlayBackValue)
    }

    const handleToggleEventTrue = () => {
        setChangePlaybackValue(true);
    }
    const handleToggleEventFalse = () =>{
        setChangePlaybackValue(false)
    }
    const handleVolumeData=(event:any)=>{
        setVolumeValue(event.target.valueAsNumber)
    }
    const handleSeek = (event:any) => {
        setIsSeeking(true)
        setSeekValue(event.target.valueAsNumber)
        setPlayDuration(event.target.valueAsNumber)
        
    }
    const [isSeeking,setIsSeeking] = useState(false);
    const [seekValue,setSeekValue] = useState(0);
    return (
        <div className="footer__player">
            {props.clickedSong?(
                <>
                    <Fullplayer setIsSeeking={setIsSeeking} seekValue={seekValue} isSeeking={isSeeking} setTotalPlayDuration={setTotalPlayDuration} setPlayDuration={setPlayDuration}  song_url={`${props.url}/${props.song_url}`} volume={volumeValue/100} playing={props.isPlayingAudio} />
                </>
            ):(
                <></>
            )}
            
            <article className="media">
                <figure className="media-left">
                    <p className="image is-96x96">
                        <img src={`${props.url}/${props.album_art}`} alt="" />
                    </p>
                </figure>
                <div className="media-content">

                    <div className="content" style={{marginBottom:0,marginTop:10}}>
                        <p className="author__name__and__song__title">
                            <strong>{props.song_name}</strong> <small>{props.author_name}</small>
                            <br />
                            
                        </p>
                        <div className='icon__container'>
                                <div className="icon__item">
                                    <div onClick={handleTenSecondsBackward} className="control__icons__backward__ten__seconds">
                                        <BackwardTenSecondsIcon color={color} width={35} height={35} />
                                    </div>
                                </div>
                                <div className="icon__item">
                                    <div className="control__icons__previous">
                                        <PreviousIcon color={color} width={38} height={38} />
                                    </div>
                                </div>
                                <div className="icon__item">
                                    <div className="control__icons__play">
                                        {!props.isPlayingAudio?(
                                            <div onClick={()=>{props.setIsPlaying(true)}}>
                                                <PlayIcon color={color} width={35} height={35} />

                                            </div>
                                        ):(
                                            <div onClick={()=>{props.setIsPlaying(false)}}>
                                                <PauseIcon color={color} width={35} height={35}/>
                                            </div>
                                        )}
                                    </div>
                                </div>
                                <div className="icon__item">
                                    <div className="control__icons__next">
                                        <NextIcon color={color} width={38} height={38}/>
                                    </div>
                                </div>
                                <div className="icon__item">
                                    <div onClick={handleTenSecondsForward} className="control__icons__forward__ten__seconds">
                                        <ForwardTenSecondsIcon color={color} width={35} height={35} />
                                    </div>  
                                </div>
                        </div>
                       
                    </div>

                    {/* Took around 16 hour to design this part */}
                    <div className="playback__grid__container level-left">
                        <div className="playback__value__div">
                            <p className="playback__grid__item playback__value">{formatTime(playDuration)}</p>
                            <p className="playback__grid__item total__playback__value">{formatTime(totalPlayDuration)}</p>
                        </div>
                        
                        <div onMouseLeave={()=>{handleToggleEventFalse()}} onMouseEnter={()=>handleToggleEventTrue()} className={`progress__bar ${changePlaybackValue?"extra__padding":""}` }>
                                
                            <div className="playback__div" >
                                {changePlaybackValue?(
                                    <>
                                    <div  className="progress__div__with__slider">
                                        <progress style={{marginTop:2}} className="progress__focus is-small progress" value={playDuration} max={totalPlayDuration} ></progress>
                                        <input  className='progress__control__slider slider is-fullwidth is-small is-circle' step={.01} min={0} max={totalPlayDuration} onChange={(event)=>handleSeek(event)} value={playDuration} type="range" />  
                                    </div>
                                    </> 
                                    ):(
                                        <div className="progress__div__with__slider">
                                            <progress style={{marginTop:2}} className="progress is-small" value={playDuration} max={totalPlayDuration}></progress>
                                        </div>
                                )}
                            </div>
                        </div>

                    </div>
                </div>
                    {/* This logic Works Perfectly */}

                    <div className="volume__icons level-left" >
                        {(showHighVolume && !showMediumVolume && !showLowVolume && !showVolumeOff && !showMute)?(
                            <VolumeHighIcon color={color} height={30} width={30} />
                        ):(showMediumVolume && !showHighVolume && !showLowVolume && !showVolumeOff && !showMute)?(
                            <VolumeMediumIcon color={color} height={30} width={30} />
                        ):(showLowVolume && !showHighVolume && !showMediumVolume && !showVolumeOff && !showMute)?(
                            <VolumeLowIcon color={color} height={30} width={30} />
                        ):(showVolumeOff && !showHighVolume && !showMediumVolume && !showLowVolume && !showMute)?(
                            <VolumeOffIcon color={color} height={30} width={30} />
                        ):(!showHighVolume && !showMediumVolume && !showLowVolume && !showVolumeOff && showMute)?(
                            <VolumeMuteIcon color={color} height={30} width={30} />
                        ):(
                            <></>
                        )}
                    </div>
                    <div className="volume__bar level-left">
                       
                        <progress style={{marginBottom:0}} className="volume__progress__level  progress is-small" value={volumeValue} max="100" ></progress>
                        <input className="volume__progress__slider slider is-fullwidth is-small is-circle" step={1} min={0} max={100} value={volumeValue} type="range" onChange={(event)=>{handleVolumeData(event)}} />
                    </div>
                    
            </article>
        </div>
    )
}