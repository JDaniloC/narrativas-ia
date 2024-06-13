import { Button } from '@/components/ui/button'
import { Chat } from '@/lib/types'

interface SubjectListProps {
  chats: Chat[],
  onSelect: (subject: string) => void
}

export function SubjectList({ chats, onSelect }: Readonly<SubjectListProps>) {
  return (
    <div className="mx-auto max-w-2xl px-4 flex flex-wrap gap-1">
      {chats.map((chat) => (
        <Button
          className="rounded-lg border bg-background p-10 grow w-1/3"
          key={chat.id}
          variant="link"
          onClick={() => onSelect(chat.id)}
        >
          {chat.title}
        </Button>
      ))}
    </div>
  )
}
