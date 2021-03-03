function SearchIcon(props: any) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 25 25"
      height={props.height}
      width={props.width}
    >
      <defs>
        <clipPath id="prefix__a">
          <path d="M1.04 1.043h22.917v22.918H1.039zm0 0" />
        </clipPath>
      </defs>
      <g clipPath="url(#prefix__a)">
        <path
          d="M16.898 14.64a8.622 8.622 0 00-2.054-12.015C10.96-.125 5.578.797 2.828 4.68a8.622 8.622 0 002.055 12.015 8.624 8.624 0 009.363.387l6.356 6.316c.687.723 1.828.75 2.55.063a1.802 1.802 0 000-2.613zm-7.039.59a5.564 5.564 0 01-5.562-5.558 5.558 5.558 0 115.566 5.559H9.86zm0 0"
          fill={props.color}
        />
      </g>
    </svg>
  );
}

export default SearchIcon;
