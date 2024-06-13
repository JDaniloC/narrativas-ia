"use client"

import React, { useState } from "react";

interface ChatContext {
  speed: number;
  canNextMsg: boolean;
  setSpeed: React.Dispatch<React.SetStateAction<number>>
  setCanNextMsg: React.Dispatch<React.SetStateAction<boolean>>
}

const ChatContext = React.createContext<ChatContext | undefined>(
  undefined
)

export function useChat() {
  const context = React.useContext(ChatContext)
  if (!context) {
    return {
      setCanNextMsg: () => {},
      setSpeed: () => {},
      canNextMsg: false,
      speed: 0,
    }
  }
  return context
}

interface ChatProviderProps {
  children: React.ReactNode;
}

export function ChatProvider({children}: Readonly<ChatProviderProps>) {
  const [canNextMsg, setCanNextMsg] = useState(false);
  const [speed, setSpeed] = useState(1);

  const contextValue = React.useMemo(() => ({
    canNextMsg,
    setCanNextMsg,
    speed, setSpeed
  }), [canNextMsg, setCanNextMsg, speed, setSpeed]);

  return (
    <ChatContext.Provider value={contextValue}>
      {children}
    </ChatContext.Provider>
  )
}