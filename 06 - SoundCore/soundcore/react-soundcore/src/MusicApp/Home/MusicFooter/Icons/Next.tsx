function NextIcon(props:any) {
    return (
      <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlnsXlink="http://www.w3.org/1999/xlink"
      width={props.width}
      height={props.height}
      version="1.1"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width={props.width}
        height={props.height}
        viewBox="0 0 30 30"
      >
        <path
          fill={props.color}
          d="M7.5 22.5L18.125 15 7.5 7.5zM20 7.5v15h2.5v-15zm0 0"
          className="color000 svgShape"
        ></path>
      </svg>
    </svg>
    );
  }
  
  export default NextIcon;