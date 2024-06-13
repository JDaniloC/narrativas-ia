
import * as React from 'react'

import { IconFastForward, IconShare } from '@/components/ui/icons'
import { Button } from '@/components/ui/button'

export interface ChatPanelProps {
  onChangeSpeed: () => void;
  onSkip: () => void;
  onNext: () => void;
  canSpeed: boolean;
  canSkip: boolean;
  canNext: boolean;
  speed: number;
}

export function Controls({
  onChangeSpeed, onSkip, onNext, canSpeed, canSkip, canNext, speed
}: Readonly<ChatPanelProps>) {
  return (
    <div id="controls" className="fixed inset-x-0 bottom-0 w-full bg-gradient-to-b from-muted/30 from-0% to-muted/30 to-50% animate-in duration-300 ease-in-out dark:from-background/10 dark:from-10% dark:to-background/80 peer-[[data-state=open]]:group-[]:lg:pl-[250px] peer-[[data-state=open]]:group-[]:xl:pl-[300px]">
      <div className="mx-auto sm:max-w-2xl sm:px-4">
        <div className="flex items-center justify-center h-12">
          <div className="flex space-x-2">
            {canSkip &&
            <Button variant="outline" onClick={onSkip} id="skip-btn">
              <IconShare className="mr-2"/>
              Pular
            </Button>}
            {canNext &&
            <Button variant="outline" onClick={onNext} id="next-btn">
              Próxima mensagem
            </Button>}
            {canSpeed &&
            <Button
              className={speed === 1 ? '' : "bg-primary text-white hover:bg-[hsl(240,6%,30%)] hover:text-white dark:bg-[hsl(240,6%,30%)] dark:hover:bg-[hsl(240,6%,30%)] dark:hover:text-white"}
              variant="ghost" size="icon"
              onClick={onChangeSpeed}
            >
              <IconFastForward/>
              <span className="sr-only"> Acelerar </span>
            </Button>}
          </div>
        </div>
      </div>
    </div>
  )
}