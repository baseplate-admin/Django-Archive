import './middle-menu.sass';

import AccountCircleOutlinedIcon from '@material-ui/icons/AccountCircleOutlined';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';

import {useEffect, useState} from "react";
import axios from 'axios';

import anime from "animejs"

const MiddleMenu = (props: any) => {
    const accountIconColor = '#dbdbdb'
    const passwordIconColor = '#dbdbdb'
    const submitButtonUnhoverColor = '#2f323a'
    const submitButtonHoverColor = '#26282f'

    const [usernameValue, setUsernameValue] = useState('');
    const [passwordValue, setPasswordValue] = useState('')

    useEffect(() => {
        anime({
            targets: '.account-icon',
            color: accountIconColor,
            easing: 'easeOutSine',
            duration: 100
        })
        anime({
            targets: '.password-icon',
            color: passwordIconColor,
            easing: 'easeOutSine',
            duration: 100
        })
    }, [])

    const handleSubmitButtonMouseEnter = (event: object) => {
        anime({
            targets: '.login-submit-button',
            backgroundColor: submitButtonHoverColor,
            easing: 'easeOutSine',
            duration: 100,
        })
    }
    const handleSubmitButtonMouseLeave = (event: object) => {
        anime({
            targets: '.login-submit-button',
            backgroundColor: submitButtonUnhoverColor,
            easing: 'easeOutSine',
            duration: 100,
        })

    }
    const handlePasswordChange = (event: string) => {
        setPasswordValue(event)
    }
    const handleUsernameChange = (event: string) => {
        setUsernameValue(event)
    }
    const handleSubmit = async (e:any) => {
        e.preventDefault()
        const payload = {"username": usernameValue, 'password': passwordValue}
        await axios.post('http://localhost:8000/api/token/', payload)
            .then(res => {
                    props.setJwt(res.data)
                }
            )
            .catch((error) => {
                    console.log(error)
                }
            )
    }
    return (
        <section className="hero login-hero is-fullheight">
            <div className="hero-body">
                <div className="container ">
                    <div className='columns is-centered is-desktop'>
                        <div className='column  is-half-desktop is-full-mobile is-three-quarters-tablet'>
                            <div className="icon-box box">
                                <div className='columns is-mobile is-centered'>
                                    <div className='column is-narrow'>
                                        <img src="https://cdn.emk.dev/templates/bulma-logo-light.png" width="150"
                                             height="40"/>
                                    </div>
                                </div>
                            </div>
                            <div className="box login-box">
                                <form onSubmit={handleSubmit}>
                                    <div className="items field is-horizontal">
                                        <div className="field-label is-normal">
                                            <label className="label">Email</label>
                                        </div>
                                        <div className="field-body">
                                            <div className="field">
                                                <p className="control is-expanded has-icons-left">
                                                    <input className="input" type="text"
                                                           placeholder="Enter your Email / Username"
                                                           onChange={(event) => {
                                                               handleUsernameChange(event.target.value)
                                                           }}
                                                    />
                                                    <span className="icon is-small is-left">
                                                    <AccountCircleOutlinedIcon className='account-icon'/>
                                                </span>
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="items field is-horizontal">
                                        <div className="field-label is-normal">
                                            <label className="label">Password</label>
                                        </div>
                                        <div className="field-body">
                                            <div className="field">
                                                <p className="control is-expanded has-icons-left">
                                                    <input className="input" type="password"
                                                           placeholder="Enter your password" onChange={(event) => {
                                                        handlePasswordChange(event.target.value)
                                                    }}/>
                                                    <span className="icon is-small is-left">
                                                    <LockOutlinedIcon className='password-icon'/>
                                            </span>
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className='items columns is-mobile is-centered'>
                                        <div className='column is-narrow'
                                             onMouseEnter={(event) => {
                                                 handleSubmitButtonMouseEnter(event.target)
                                             }}
                                             onMouseLeave={(event) => {
                                                 handleSubmitButtonMouseLeave(event.target)
                                             }}>
                                            <button type="submit"
                                                    className="button is-rounded is-centered login-submit-button"

                                            >Sign in
                                            </button>
                                        </div>
                                    </div>

                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}
export default MiddleMenu;