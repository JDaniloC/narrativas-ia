"use client";

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle
} from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Chat } from '@/lib/types';
import { useEffect, useState } from 'react';
import { useSubject } from '../subject-context';

interface ModalSubjectProps {
  chat: Chat | null
}


export default function ModalSubject({ chat }: Readonly<ModalSubjectProps>) {
  const [showDialog, setShowDialog] = useState(true);
  const { title, setTitle } = useSubject();

  useEffect(() => {
    if (chat?.title) setTitle(chat.title);
  }, [])

  function handleSave() {
    if (title) setShowDialog(false);
  }

  return (
    <Dialog open={showDialog}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle> Criador de assuntos </DialogTitle>
          <DialogDescription>
            Aqui você pode criar conversas para serem exibidas na plataforma. Escolha o nome do assunto e clique em salvar. Você pode voltar para editar esse assunto ao entrar nesta página pelo seu ID.
          </DialogDescription>
        </DialogHeader>
        <Input
          value={title}
          placeholder="Digite o título do assunto"
          onChange={e => setTitle(e.target.value)}
        />
        <DialogFooter className="items-center">
          <Button onClick={handleSave}>
            Salvar
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}