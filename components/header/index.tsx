import * as React from 'react'
import { ShareSiteButton } from './share-button'
import { buttonVariants } from '@/components/ui/button'
import { cn } from '@/lib/utils'
import Link from 'next/link';
import { ThemeToggle } from './theme-toggle';

export function Header() {
  return (
    <header className="sticky top-0 z-50 flex items-center justify-between w-full h-16 px-4 border-b shrink-0 bg-gradient-to-b from-background/10 via-background/50 to-background/80 backdrop-blur-xl">
      <div>
        <Link
          href={"/"}
          className={cn(
            buttonVariants({ variant: 'ghost' }),
            'group w-full px-8 transition-colors hover:bg-zinc-200/40 dark:hover:bg-zinc-300/10'
          )}
        >
          Galeria
        </Link>
      </div>
      <div className="flex items-center justify-end space-x-2" id="share">
        <ThemeToggle/>
        <ShareSiteButton/>
      </div>
    </header>
  )
}
