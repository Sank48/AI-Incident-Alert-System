export function Badge({ children, variant = "solid" }) {
  const base = "inline-block text-xs px-2 py-1 rounded-full font-medium";
  const variants = {
    solid: "bg-blue-600 text-white",
    outline: "border border-blue-600 text-blue-600",
  };
  return <span className={`${base} ${variants[variant]}`}>{children}</span>;
}
