"use client"

import { cn } from "clsx-for-tailwind";
import { useCallback, useEffect, useId, useRef, useState } from "react";

const GRID_PATH =
  "M96.5 -47.5V47.5H192.5M336.5 47.5H432.5V287.5M336.5 47.5V-47.5M336.5 47.5V95.5H192.5M432.5 287.5H336.5V432.5M432.5 287.5V432.5M432.5 287.5H480.5H576.5M0.5 -47.5V95.5H48.5V191.5H192.5V432.5M192.5 95.5H144.5V287.5H0.5V432.5M192.5 95.5V47.5M192.5 -47.5V47.5M240.5 95.5V143.5V335.5H480.5V432.5M576.5 95.5V-47.5M576.5 95.5H720.5V-47.5M576.5 95.5V239.5M576.5 432.5V287.5M576.5 239.5H720.5V432.5M576.5 239.5V287.5";

// Path viewBox dimensions
const PATH_W = 721;
const PATH_H = 432;

interface LogoRevealProps {
  gridBgSrc?: string;
  className?: string;
  revealRadius?: number;
  strokeWidth?: number;
}

export function LogoReveal({
  gridBgSrc = "/common/light/squares_logo.svg",
  className,
  revealRadius = 180,
  strokeWidth = 2,
}: LogoRevealProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [mouse, setMouse] = useState({ x: -9999, y: -9999 });
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });
  const uniqueId = useId();

  // Calculate offsets to center the path within the background
  const offsetX = (dimensions.width - PATH_W) / 2;
  const offsetY = (dimensions.height - PATH_H) / 2;

  const updateDimensions = useCallback(() => {
    const img = containerRef.current?.querySelector("img");
    if (img && img.naturalWidth && img.naturalHeight) {
      setDimensions({ width: img.naturalWidth, height: img.naturalHeight });
    }
  }, []);

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      const el = containerRef.current;
      if (!el || !dimensions.width || !dimensions.height) return;
      const rect = el.getBoundingClientRect();
      const scaleX = dimensions.width / rect.width;
      const scaleY = dimensions.height / rect.height;
      setMouse({
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY,
      });
    },
    [dimensions]
  );

  const handleMouseLeave = useCallback(() => {
    setMouse({ x: -9999, y: -9999 });
  }, []);

  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    el.addEventListener("mousemove", handleMouseMove);
    el.addEventListener("mouseleave", handleMouseLeave);

    return () => {
      el.removeEventListener("mousemove", handleMouseMove);
      el.removeEventListener("mouseleave", handleMouseLeave);
    };
  }, [handleMouseMove, handleMouseLeave]);

  // Unique IDs for SVG elements to avoid conflicts with multiple instances
  const revealGradId = `revealGrad-${uniqueId}`;
  const revealMaskId = `revealMask-${uniqueId}`;
  const purpleStrokeId = `purpleStroke-${uniqueId}`;
  const lineGlowId = `lineGlow-${uniqueId}`;

  return (
    <div ref={containerRef} className={cn("relative w-full", className)}>
      {/* Background squares grid */}
      <img
        src={gridBgSrc}
        alt=""
        className="w-full h-auto pointer-events-none select-none"
        draggable={false}
        onLoad={updateDimensions}
      />

      {/* Foreground SVG with reveal effect */}
      {dimensions.width > 0 && dimensions.height > 0 && (
        <svg
          className="absolute inset-0 w-full h-full pointer-events-none"
          viewBox={`0 0 ${dimensions.width} ${dimensions.height}`}
          preserveAspectRatio="xMidYMid meet"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <radialGradient id={revealGradId} cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="white" stopOpacity="1" />
              <stop offset="55%" stopColor="white" stopOpacity="0.5" />
              <stop offset="100%" stopColor="white" stopOpacity="0" />
            </radialGradient>

            <mask id={revealMaskId}>
              <rect
                width={dimensions.width}
                height={dimensions.height}
                fill="black"
              />
              <circle
                cx={mouse.x}
                cy={mouse.y}
                r={revealRadius}
                fill={`url(#${revealGradId})`}
              />
            </mask>

            <radialGradient
              id={purpleStrokeId}
              gradientUnits="userSpaceOnUse"
              cx={mouse.x - offsetX}
              cy={mouse.y - offsetY}
              r={revealRadius}
            >
              <stop offset="0%" stopColor="#654DC4" />
              <stop offset="49.52%" stopColor="#D4CAFE" />
              <stop offset="100%" stopColor="#6E56CF" />
            </radialGradient>

            <filter id={lineGlowId} x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="5" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
          </defs>

          <g mask={`url(#${revealMaskId})`}>
            <g
              transform={`translate(${offsetX}, ${offsetY})`}
              filter={`url(#${lineGlowId})`}
            >
              <path
                d={GRID_PATH}
                stroke={`url(#${purpleStrokeId})`}
                strokeWidth={strokeWidth}
              />
            </g>
          </g>
        </svg>
      )}
    </div>
  );
}

export default LogoReveal;
