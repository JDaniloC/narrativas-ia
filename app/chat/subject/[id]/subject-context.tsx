"use client"

import React, { useState } from "react";
import { MessageStream } from "@/lib/types";

interface SubjectContext {
  title: string;
  messages: MessageStream[];
  removeLastMessage: () => void;
  setTitle: (newTitle: string) => void
  addMessage: (message: MessageStream) => void;
}

const SubjectContext = React.createContext<SubjectContext | undefined>(
  undefined
)

export function useSubject() {
  const context = React.useContext(SubjectContext)
  if (!context) {
    throw new Error('useSubjectContext must be used within a SubjectProvider')
  }
  return context
}

interface SubjectProviderProps {
  chatMessages: MessageStream[];
  children: React.ReactNode;
}

export function SubjectProvider({
  children, chatMessages
}: Readonly<SubjectProviderProps>) {
  const [title, setTitle] = useState("");
  const [messages, setMessages] = useState<MessageStream[]>(chatMessages);

  function addMessage(message: MessageStream) {
    setMessages(prev => [...prev, {
      ...message,
      id: String(prev.length + 1),
    }]);
  }

  function removeLastMessage() {
    if (messages.length === 0) return;
    setMessages(prev => prev.slice(0, prev.length - 1));
  }

  const contextValue = React.useMemo(() => ({
    title,
    setTitle,
    messages,
    addMessage,
    removeLastMessage
  }), [title, setTitle, messages, addMessage, removeLastMessage]);

  return (
    <SubjectContext.Provider value={contextValue}>
      {children}
    </SubjectContext.Provider>
  )
}