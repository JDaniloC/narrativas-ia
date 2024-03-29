import { type Message } from 'ai'

export interface Chat extends Record<string, any> {
  id: string
  title: string
  createdAt: Date
  userId: string
  path: string
  messages: Message[]
  sharePath?: string
}

export interface MessageStream {
  id: string
  role: string
  content: string
  isFinished?: boolean
}

export interface Page {
  id: string
  name: string
  href: string
}

export type ServerActionResult<Result> = Promise<
  | Result
  | {
      error: string
    }
>
