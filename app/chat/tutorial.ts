import { driver } from "driver.js";

export const chatTutorial = driver({
  showProgress: true,
  steps: [
    {
      popover: {
        title: 'Tour da página',
        description: 'Hey, deixa eu te explicar rapidinho como funciona a página?'
      }
    },
    {
      element: '#page-list',
      popover: {
        title: 'Lista de páginas',
        description: 'Aqui você pode entrar em outras páginas e visualizar o conteúdo de outra maneira.',
      }
    },
    {
      element: '#chat-content',
      popover: {
        title: 'Conteúdo',
        description: 'Aqui será exibido uma conversa roteirizada, de forma a apresentar o conteúdo.'
      }
    },
    {
      element: '#controls',
      popover: {
        title: 'Controles',
        description: 'Aqui você pode controlar o andamento da conversa: pular, acelerar e avançar.',
        side: "top",
        align: 'center'
      },
    },
    {
      element: '#skip-btn',
      popover: {
        title: 'Pular a conversa',
        description: 'Ao clicar neste botão irá pular toda a conversa e ir para a seleção de novos assuntos'
      }
    },
    {
      element: '#next-btn',
      popover: {
        title: 'Avançar conversa',
        description: 'Para avançar na conversa, você pode clicar neste botão ou teclar espaço, enter ou a seta para baixo/direita'
      }
    },
    {
      element: '#share',
      popover: {
        title: 'Compartilhar',
        description: 'Se você gostou, compartilha para informar mais uma pessoa!'
      },
    },
  ]
});
