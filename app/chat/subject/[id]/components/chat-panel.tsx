import * as React from 'react'

import { FooterText } from './footer'
import PromptForm from './prompt-form'
import { ButtonScrollToBottom } from './button-scroll-to-bottom'

import { IconPlus, IconStop } from '@/components/ui/icons'
import { UseChatHelpers } from 'ai/react/dist';
import { Button } from '@/components/ui/button'
import { MessageStream } from '@/lib/types';

export interface ChatPanelProps
  extends Pick<
    UseChatHelpers,
    | 'input'
    | 'setInput'
  > {
  onSave: () => void;
  onRemove: () => void;
  onChangeRole: () => void
  messages: MessageStream[];
  onSubmit: (content: string) => void;
}

export function ChatPanel({
  input,
  messages,
  setInput,
  onChangeRole,
  onSubmit,
  onRemove,
  onSave,
}: Readonly<ChatPanelProps>) {
  return (
    <div className="fixed inset-x-0 bottom-0 w-full bg-gradient-to-b from-muted/30 from-0% to-muted/30 to-50% animate-in duration-300 ease-in-out dark:from-background/10 dark:from-10% dark:to-background/80 peer-[[data-state=open]]:group-[]:lg:pl-[250px] peer-[[data-state=open]]:group-[]:xl:pl-[300px]">
      <ButtonScrollToBottom />
      <div className="mx-auto sm:max-w-2xl sm:px-4">
        <div className="flex items-center justify-center h-12">
          <div className="flex space-x-2">
            {messages?.length >= 2 && (
              <Button variant="outline" onClick={onSave}>
                <IconPlus className="mr-2"/>
                Salvar assunto
              </Button>
            )}
            <Button variant="outline" onClick={onRemove}>
              <IconStop className="mr-2"/>
              Refazer mensagem
            </Button>
          </div>
        </div>
        <div className="px-4 py-2 space-y-4 border-t shadow-lg bg-background sm:rounded-t-xl sm:border md:py-4">
          <PromptForm
            input={input}
            isLoading={false}
            setInput={setInput}
            onSubmit={onSubmit}
            changeRole={onChangeRole}
          />
          <FooterText className="hidden sm:block" />
        </div>
      </div>
    </div>
  )
}
