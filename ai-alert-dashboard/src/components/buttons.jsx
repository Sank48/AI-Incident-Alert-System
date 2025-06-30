// export default function Button({ text }) {
//   return <div className="btn">{text}</div>;
// }

export default function Button({
  children,
  onClick,
  size = "base",
  variant = "solid",
}) {
  const base = "px-4 py-2 rounded-xl font-medium shadow-sm";
  const sizes = {
    sm: "text-sm py-1 px-3",
    base: "text-base",
  };
  const variants = {
    solid: "bg-gray-700 text-white hover:bg-gray-800",
    outline: "border border-blue-600 text-blue-600 hover:bg-blue-100",
  };
  return (
    <button
      onClick={onClick}
      className={`${base} ${sizes[size]} ${variants[variant]}`}
    >
      {children}
    </button>
  );
}
