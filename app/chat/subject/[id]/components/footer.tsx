import React from 'react'

import { cn } from '@/lib/utils'
import { ExternalLink } from '@/components/external-link'

export function FooterText({ className, ...props }: React.ComponentProps<'p'>) {
  return (
    <p
      className={cn(
        'px-2 text-center text-xs leading-normal text-muted-foreground',
        className
      )}
      {...props}
    >
      Um projeto produzido para a disciplina de&nbsp;
      <ExternalLink href="https://visse.vercel.app/">
        Narrativas Inovadoras com Dados na Comunicação Digital
      </ExternalLink>.
    </p>
  )
}
