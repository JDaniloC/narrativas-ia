'use client'

import { SubjectList } from './subject-list'
import { ChatList } from '@/components/chat-list'
import { ChatScrollAnchor } from '@/components/chat-scroll-anchor'
import { Chat, MessageStream } from '@/lib/types'
import { useCallback, useEffect, useState } from 'react'
import { Controls } from './controls'
import { useChat } from '../chat-context'
import { useKeyPress } from '../../../lib/hooks/use-key-down'
import { chatTutorial } from '../tutorial'
import { useLocalStorage } from '../../../lib/hooks/use-local-storage'

export interface ChatProps extends React.ComponentProps<'div'> {
  chats: Chat[],
}

export default function ChatComponent({ chats }: Readonly<ChatProps>) {
  const [_, setTutorial] = useLocalStorage("chat-tutorial", true);
  const { canNextMsg, setCanNextMsg, speed, setSpeed } = useChat();

  const [allMessages, setAllMessages] = useState<MessageStream[]>([]);
  const [availableChats, setAvailableChats] = useState<Chat[]>(chats);
  const [messages, setMessages] = useState<MessageStream[]>([]);
  const [index, setIndex] = useState(0);

  const loadNewSubject = useCallback((chatID: string) => {
    const chat = availableChats.find(chat => chat.id === chatID);
    if (!chat) return;

    setIndex(prev => prev + 1);
    setMessages(prev => [...prev, chat.messages[0]]);
    setAllMessages(prev => [...prev, ...chat.messages]);
    setAvailableChats(prev => prev.filter(c => c.id !== chatID));
  }, [availableChats]);

  useEffect(() => {
    if (chats.length === 0) return;
    setIndex(0);
    setMessages([]);
    setAllMessages([]);
    setAvailableChats(chats);
    loadNewSubject("0");
  }, [chats]);

  useEffect(() => {
    const tutorial = window.localStorage.getItem("chat-tutorial");
    if (!tutorial) {
      chatTutorial.drive();
      setTutorial(true);
    }
  }, [setTutorial])

  function nextMessage() {
    if (index >= allMessages.length || !canNextMsg) return;
    setMessages(prev => [...prev, allMessages[index]]);
    setIndex(prev => prev + 1);
    if (speed > 1) setSpeed(1);
    setCanNextMsg(false);
  }

  function skipToEnd() {
    setMessages(prev => [...prev, ...allMessages.slice(index)]);
    setIndex(allMessages.length);
  }

  function changeSpeed() {
    setSpeed(prev => prev === 1 ? 8 : 1);
  }

  useKeyPress(() => {
    if (canNextMsg) nextMessage();
  }, ["ArrowRight", "Enter", " ", "ArrowDown"]);

  return (
    <div className='pb-[200px] pt-4 md:pt-10' id="chat-content">
      <ChatList messages={messages}/>
      <Controls
        speed={speed}
        onSkip={skipToEnd}
        onNext={nextMessage}
        onChangeSpeed={changeSpeed}
        canSpeed={!canNextMsg}
        canSkip={index < allMessages.length}
        canNext={canNextMsg && index < allMessages.length}
      />
      <ChatScrollAnchor trackVisibility={!canNextMsg}/>
      {availableChats.length > 0 && index === allMessages.length && canNextMsg &&
        <SubjectList onSelect={loadNewSubject} chats={availableChats}/>}
    </div>
  )
}
