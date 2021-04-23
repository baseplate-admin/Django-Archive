import "./right-sidebar.sass"

const RightAside = () => {
    return(
        <section className="hero is-fullheight-with-navbar right-menu-fullheight">
            <aside className="menu">
                {/* For Loop starts here */}
                <article className="media ">
                    <figure className="media-left">
                        <p className="image is-64x64">
                        <img className="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" />
                        </p>
                    </figure>
                    <div className="media-content">
                        <div className="content">
                        <p>
                            <strong>John Smith</strong> 
                            <br />
                            <div className='reply'>
                                You: Hello World

                            </div>
                        </p>
                        </div>
                    </div>
                </article>
                <hr />
            </aside>
        </section>
    )
}
export default RightAside;