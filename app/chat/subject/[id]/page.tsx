import { type Metadata } from 'next'

import { getSharedChat } from '@/app/actions'
import { SubjectProvider } from './subject-context';
import ModalSubject from './components/modal-subject';
import Subject from './components/subject';

interface SharePageProps {
  params: {
    id: string
  }
}

export async function generateMetadata({
  params
}: SharePageProps): Promise<Metadata> {
  const chat = await getSharedChat(params.id)

  return {
    title: chat?.title.slice(0, 50) ?? 'Editor de temas'
  }
}

export default async function SubjectPage({
  params
}: Readonly<SharePageProps>) {
  const chat = await getSharedChat(params.id);

  const messages = chat?.messages ?? [];

  return (
    <SubjectProvider chatMessages={messages}>
      <Subject id={params.id}/>
      <ModalSubject chat={chat ?? null}/>
    </SubjectProvider>
  )
}
