import {useEffect, useState} from "react";

// Anime for Button coloring
import anime from "animejs";

// Tippy for toolbar positioning
import "react-tippy/dist/tippy.css"
import {Tooltip} from "react-tippy";

import useLocalStorage from "react-use-localstorage";

// Importing All the icons
import PhoneIcon from "@material-ui/icons/Phone";
import VideocamTwoToneIcon from "@material-ui/icons/VideocamTwoTone";
import SendIcon from "@material-ui/icons/Send";
import EmojiEmotionsIcon from "@material-ui/icons/EmojiEmotions";
import AddCircleOutlineOutlinedIcon from '@material-ui/icons/AddCircleOutlineOutlined';

// Main SASS import
import "./middle-column.sass"

//History API from react router for redirect
import {useHistory} from 'react-router-dom';
// Axios Post
import axios from 'axios';

const MiddleColumn = () => {
    const [accessToken, setAccessToken] = useLocalStorage('a_key')
    const [refreshToken, setRefreshToken] = useLocalStorage('r_key')
    useEffect(() => {
        setInterval(() => {
            const url = 'http://127.0.0.1:8000/api/token/refresh/'
            axios.post(url, {'refresh': refreshToken})
                .then(res => {
                    setAccessToken(res.data.access)
                })
                .catch(error => {
                    alert(error)
                })
        }, 5000)
    }, [refreshToken])
    //  Color For the Icons
    // The colors are picked from Bulma Docs

    /* 
        Hex Decoder
            #ffe08a = yellow  <-- Used on the emoji 
            #48c78e = green   <-- Used on all the other icons
    */
    const callIconHoverColor = '#3e8ed0'
    const videoIconHoverColor = '#3e8ed0'
    const emojiIconHoverColor = '#ffe08a'
    const sendIconHoverColor = '#48c78e'
    const addIconHoverColor = '#3e8ed0'

    const callIconUnhoverColor = '#dbdbdb'
    const videoIconUnhoverColor = '#dbdbdb'
    const emojiIconUnhoverColor = '#dbdbdb'
    const sendIconUnhoverColor = '#dbdbdb'
    const addIconUnhoverColor = '#dbdbdb'
    const [input, setInput] = useState('');

    const [socket, setSocket] = useState(Object)
    useEffect(() => {
        setSocket(new WebSocket('ws://localhost:8000/api/v1/front/'))
    }, [])
    const history = useHistory();

    socket.onopen = () => {
        console.log('Connected To Django Server')
    }
    socket.onclose = () => {
        console.log("Disconnected From Backend :( !")
        setSocket(Object)
    }

    const handleSendClick = () => {
        if (input === '') {
            console.log('You must write something.')
        } else {
            if (accessToken && refreshToken) {
                const jwt = {
                    'refresh': refreshToken,
                    'access': accessToken,
                }
                const payload =
                    {
                        'input': input,
                        'jwt': jwt
                    }

                const jsonData = JSON.stringify(payload)

                socket.send(jsonData)
                setInput('')
            } else if (!accessToken && !refreshToken) {
                history.push('/login')
            }
        }
    }

    const handleInputChange = (input: string) => {
        setInput(input)
    }

    useEffect(() => {
        anime({
            targets: ".video-icon",
            color: videoIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
        anime({
            targets: '.phone-icon',
            color: callIconUnhoverColor,
            easing: "easeOutSine",
            duration: 100
        })
        anime({
            targets: '.send-icon-main',
            color: sendIconUnhoverColor,
            easing: "easeOutSine",
            duration: 100
        })
        anime({
            targets: '.emoji-picker',
            color: emojiIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100,
        })
        anime({
            targets: '.add-icon',
            color: addIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    })

    /* 
        Emoji Mouse Effect Handler
            handleEmojiIconMouseEnter = Handles mouse entering emoji
            handleEmojiIconMouseLeave = Handles mouse leaving emoji
    */

    const handleEmojiIconMouseEnter = (event: object) => {
        anime({
            targets: '.emoji-picker',
            color: emojiIconHoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }
    const handleEmojiIconMouseLeave = (event: object) => {
        anime({
            targets: '.emoji-picker',
            color: emojiIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }

    /* 
        Phone Icon Mouse Effect Handler
    */

    const handlePhoneIconMouseEnter = (event: object) => {
        anime({
            targets: '.phone-icon',
            color: callIconHoverColor,
            easing: "easeOutSine",
            duration: 100
        })
    }

    const handlePhoneIconMouseLeave = (event: object) => {
        anime({
            targets: '.phone-icon',
            color: callIconUnhoverColor,
            easing: "easeOutSine",
            duration: 100

        })
    }

    /* 
        Video Icon Mouse Effect Handler
    */

    const handleVideoIconMouseEnter = (event: object) => {
        anime({
            targets: ".video-icon",
            color: videoIconHoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }

    const handleVideoIconMouseLeave = (event: object) => {
        anime({
            targets: ".video-icon",
            color: videoIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }

    /*
        Add Icon Mouse Effect Handler
    */

    const handleAddIconMouseEnter = (event: object) => {
        anime({
            targets: ".add-icon",
            color: addIconHoverColor,
            easing: 'easeOutSine',
            duration: 100,
        })
    }

    const handleAddIconMouseLeave = (event: object) => {
        anime({
            targets: '.add-icon',
            color: addIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }

    /* 
        Send Icon Mouse Effect Handler
    */

    const handleSendIconMouseEnter = (event: object) => {
        anime({
            targets: '.send-icon-main',
            color: sendIconHoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }

    const handleSendIconMouseLeave = (event: object) => {
        anime({
            targets: '.send-icon-main',
            color: sendIconUnhoverColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }
    // Render the html

    return (
        <section className="hero is-fullheight-with-navbar middle-menu-fullheight">
            <div className="columns is-mobile is-vcentered" id="up">
                <div className="column">
                    <article className="media">
                        <figure className="media-left">
                            <p className="image is-64x64">
                                <img alt="user" className="is-rounded"
                                     src="https://bulma.io/images/placeholders/128x128.png"/>
                            </p>
                        </figure>
                        <div className="media-content">
                            <div className="content">
                                <span>
                                    <strong>John Smith</strong>
                                </span>
                            </div>
                        </div>
                        <div className="media-right">
                            <div className="item" onMouseEnter={(event) => {
                                handlePhoneIconMouseEnter(event)
                            }} onMouseLeave={(event) => {
                                handlePhoneIconMouseLeave(event)
                            }}>
                                <Tooltip
                                    animateFill
                                    title="Call"
                                    position="bottom"
                                    trigger="mouseenter"
                                    arrow
                                    animation="fade"
                                >
                                    <button className='phone-icon-wrapper'>
                                        <PhoneIcon
                                            className='phone-icon'
                                        />

                                    </button>
                                </Tooltip>
                            </div>
                            <div className="item" onMouseEnter={(event) => {
                                handleVideoIconMouseEnter(event)
                            }} onMouseLeave={(event) => {
                                handleVideoIconMouseLeave(event)
                            }}>
                                <Tooltip
                                    animateFill
                                    title="Video Call"
                                    position="bottom"
                                    trigger="mouseenter"
                                    arrow
                                    animation="fade"

                                >
                                    <button className='video-icon-wrapper'>
                                        <VideocamTwoToneIcon
                                            className='video-icon'
                                        />
                                    </button>
                                </Tooltip>
                            </div>
                        </div>
                    </article>
                </div>
            </div>
            <div id="middle">
                <div className="box">
                    <div className="scroll">
                        {/* Input chat elements go inside of here. */}
                    </div>
                </div>
            </div>
            <div id="last">
                <div className="columns is-mobile is-vcentered">
                    <div className="column is-1"></div>

                    <div className="column input-column">
                        <div className="control has-icons-right has-icons-left">
                            <input
                                className="input is-rounded is-normal"
                                type="text"
                                placeholder="Text input"
                                value={input}
                                onChange={event => handleInputChange(event.target.value)}
                            />
                            <span className="is-small icon is-right"
                                  onMouseEnter={(event) => {
                                      handleEmojiIconMouseEnter(event)
                                  }}
                                  onMouseLeave={(event) => {
                                      handleEmojiIconMouseLeave(event)
                                  }}
                            >
                                <Tooltip
                                    animateFill
                                    title="Emoji"
                                    position="top"
                                    trigger="mouseenter"
                                    arrow
                                    animation="fade"
                                >
                                    <EmojiEmotionsIcon
                                        className="emoji-picker"
                                    />
                                </Tooltip>
                            </span>
                            <span className='is-small icon is-left' onMouseEnter={(event) => {
                                handleAddIconMouseEnter(event)
                            }} onMouseLeave={(event) => {
                                handleAddIconMouseLeave(event)
                            }}>
                                <Tooltip
                                    animateFill
                                    title="Add Items"
                                    position="top"
                                    trigger="mouseenter"
                                    arrow
                                    animation="fade"
                                >
                                    <AddCircleOutlineOutlinedIcon
                                        className='add-icon'
                                    />
                                </Tooltip>
                            </span>
                        </div>
                    </div>
                    <div className="column is-narrow send-icon"
                         onMouseEnter={(event) => {
                             handleSendIconMouseEnter(event)
                         }}
                         onMouseLeave={(event) => {
                             handleSendIconMouseLeave(event)
                         }}
                         onClick={handleSendClick}
                    >
                        <Tooltip
                            animateFill
                            title="Send"
                            position="top"
                            trigger="mouseenter"
                            arrow
                            animation="fade"
                        >
                            <button className=" button is-rounded">
                                <SendIcon
                                    className="send-icon-main"
                                />
                            </button>
                        </Tooltip>
                    </div>
                </div>
            </div>

        </section>
    )
}
export default MiddleColumn;