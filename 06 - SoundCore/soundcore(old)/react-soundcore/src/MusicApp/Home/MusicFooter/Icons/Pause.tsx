function PauseIcon(props:any) {
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
          d="M11.25 20h2.5V10h-2.5zM15 2.5C8.102 2.5 2.5 8.102 2.5 15S8.102 27.5 15 27.5 27.5 21.898 27.5 15 21.898 2.5 15 2.5zM15 25C9.488 25 5 20.512 5 15S9.488 5 15 5s10 4.488 10 10-4.488 10-10 10zm1.25-5h2.5V10h-2.5zm0 0"
          className="color000 svgShape"
        ></path>
      </svg>
    </svg>
    );
  }
  
export default PauseIcon;
  