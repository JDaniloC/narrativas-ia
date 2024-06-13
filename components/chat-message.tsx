import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'

import { cn } from '@/lib/utils'
import { MemoizedReactMarkdown } from '@/components/markdown'
import { IconOpenAI, IconUser } from '@/components/ui/icons'
import { ChatMessageActions } from '@/components/chat-message-actions'
import { MessageStream } from '../lib/types'
import { useEffect, useState } from 'react'
import { useChat } from '../app/chat/chat-context'

export interface ChatMessageProps {
  message: MessageStream
  renderAnimation?: boolean
}

export function ChatMessage({
  message, renderAnimation, ...props
}: Readonly<ChatMessageProps>) {
  const [currentText, setCurrentText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const { speed, setCanNextMsg } = useChat();
  const content = message.content;

  useEffect(() => {
    if (speed === 0 || !renderAnimation) return setCurrentText(content);

    if (currentIndex < content.length) {
      const timeout = setTimeout(() => {
        setCurrentText(prevText => prevText + content[currentIndex]);
        setCurrentIndex(prevIndex => prevIndex + 1);
      }, 20 / speed);

      return () => clearTimeout(timeout);
    } else {
      setCanNextMsg(true);
    }
  }, [currentIndex, content]);

  return (
    <div
      className={cn('group relative mb-4 flex items-start md:-ml-12')}
      {...props}
    >
      <div
        className={cn(
          'flex size-8 shrink-0 select-none items-center justify-center rounded-md border shadow',
          message.role === 'user'
            ? 'bg-background'
            : 'bg-primary text-primary-foreground'
        )}
      >
        {message.role === 'user' ? <IconUser /> : <IconOpenAI />}
      </div>
      <div className="flex-1 px-1 ml-4 space-y-2 overflow-hidden">
        <MemoizedReactMarkdown
          className="prose break-words dark:prose-invert prose-p:leading-relaxed prose-pre:p-0"
          remarkPlugins={[remarkGfm, remarkMath]}
          components={{
            p({ children }) {
              return <p className="mb-2 last:mb-0">{children}</p>
            },
          }}
        >
          {currentText}
        </MemoizedReactMarkdown>
        <ChatMessageActions message={message} />
      </div>
    </div>
  )
}
