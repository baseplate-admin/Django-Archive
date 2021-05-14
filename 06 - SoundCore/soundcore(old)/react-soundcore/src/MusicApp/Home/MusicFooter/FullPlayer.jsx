import React, { Component } from 'react'

import ReactHowler from 'react-howler'

class Fullplayer extends Component{
  constructor (props) {
    super(props)
    this.state = {
        loop: false,
        mute: false,
        volume: 1.0,
        seek: 0.0,
    }
    this.setSeek = this.setSeek.bind(this)
    this.handlePlay = this.handlePlay.bind(this)
    this.handlePause = this.handlePause.bind(this)
    this.handleSeek = this.handleSeek.bind(this)
    this.handeleLoad = this.handeleLoad.bind(this)
  }
    handeleLoad(){
        this.props.setTotalPlayDuration(this.player.duration())
    }

    handlePlay(){

    }
    componentDidUpdate(){
      if(!this.props.isSeeking){
        setInterval(()=>{
          this.handleSeek()
        },1)
      }
      else if (this.props.isSeeking){
        this.player.stop()
        this.setSeek()
        this.player.play()
        this.props.setIsSeeking(false)
      }
    }

    handlePause(){

    }

    handleSeek(){
      this.props.setPlayDuration(this.player.seek())
    }
    
    
    setSeek () {
      this.player.seek(parseFloat(this.props.seekValue))
    }
      // This sound file may not work due to cross-origin setting
      render () {
        return(
            <>
          <ReactHowler
            src={this.props.song_url}
            playing={this.props.playing}
            volume={this.props.volume}
            onLoad={this.handeleLoad}
            onPlay={this.handlePlay}
            onPause={this.handlePause}
            ref={ref=>{this.player=ref}}
          />
          </>
        );
      }
    }

export default Fullplayer


// Notes

// this.player.seek()  = Returns Playback Position
// this.player.duration() = Returns Playback duration 
// this.player.isSeeking() = Donno dont care