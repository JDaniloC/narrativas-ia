import Chat from './components/chat'
import { getChats } from '../actions';
import { ChatProvider } from './chat-context';

export default async function IndexPage() {
  const chats = (await getChats("global"))
    .sort((a, b) => a.id <= b.id ? 0 : 1);

  return (
    <ChatProvider>
      <Chat chats={chats} />
    </ChatProvider>
  )
}
