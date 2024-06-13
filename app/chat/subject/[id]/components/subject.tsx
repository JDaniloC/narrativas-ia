"use client";

import { useState } from "react";

import { ChatPanel } from "./chat-panel";
import { MessageStream } from "@/lib/types";
import { ChatList } from "@/components/chat-list";
import { ChatScrollAnchor } from "@/components/chat-scroll-anchor";

import { useSubject } from "../subject-context";
import { toast } from 'react-hot-toast'

interface SubjectProps {
  id: string;
}

async function postSubject(
  id: string, title: string, messages: MessageStream[]
) {
  const response = await fetch("/api/subject/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ id, title, messages })
  });

  if (!response.ok) {
    throw new Error("Failed to save subject");
  }
}

export default function Subject({ id }: Readonly<SubjectProps>) {
  const { messages, title, addMessage, removeLastMessage } = useSubject();
  const [role, setRole] = useState("user");
  const [input, setInput] = useState("");

  function handleChangeRole() {
    setRole(role === "user" ? "assistant" : "user");
  }

  function handleSubmit(content: string) {
    const message: MessageStream = {
      id: String(messages.length + 1),
      content, role
    }
    addMessage(message);
    handleChangeRole();
  }

  function handleSave() {
    postSubject(id, title, messages);
    toast.success(`Assunto ${title} salvo!`);
  }

  return (
    <div className='pb-[200px] pt-4 md:pt-10'>
      <ChatList messages={messages}/>
      <ChatScrollAnchor trackVisibility={true} />
      <ChatPanel
        input={input}
        messages={messages}
        setInput={setInput}
        onSave={handleSave}
        onSubmit={handleSubmit}
        onRemove={removeLastMessage}
        onChangeRole={handleChangeRole}
      />
    </div>
  )
}