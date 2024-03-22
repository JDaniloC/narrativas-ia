import React from 'react';
import styles from './styles.module.css'
import Image from 'next/image';
import { blockMoldure2Img } from '../problema-images';


const MyComponent: React.FC = () => {

    const text = "Algoritmos de IA também desempenham um papel vital na segurança digital, identificando padrões incomuns que podem indicar atividades fraudulentas. Isso é crucial para a proteção dos usuários em transações financeiras online e na prevenção de ataques cibernéticos.Andrew Ng, um destacado cientista da computação e defensor da inteligência artificial, ressalta que esses avanços não apenas melhoram a eficiência dos sistemas, mas também contribuem para a segurança e conveniência dos usuários, promovendo uma experiência digital mais fluida e segura."
    const text2 = "No entanto, a coleta extensiva de dados pode resultar em violações de privacidade, especialmente quando as medidas de segurança não são suficientes. Vazamentos de informações pessoais são uma ameaça constante, expondo usuários a riscos de roubo de identidade e outros crimes cibernéticos."
    const text3 = "Algoritmos de IA podem herdar e amplificar os preconceitos presentes nos dados de treinamento, resultando em discriminação injusta, exacerbando disparidades sociais e prejudicando grupos minoritários. A falta de transparência dos algoritmos levanta questões sobre a compreensão e o controle que os usuários têm sobre o uso de seus dados. A ausência de transparência pode minar a confiança do público e criar um ambiente onde as decisões automatizadas não são compreendidas."
    const text4 = "A Inteligência Artificial é como ensinamos computadores a pensar e aprender como seres humanos. É uma tecnologia que ajuda as máquinas a entenderem coisas. Mas, assim como tem pontos positivos, também pode ter desafios, como quando queremos manter nossas informações privadas, evitar decisões injustas ou entender como os computadores tomam decisões."
    const text5 = "Um dos pontos mais destacados é a capacidade da IA de personalizar serviços com base na análise de dados. Plataformas de streaming, por exemplo, utilizam algoritmos para entender os gostos dos usuários, oferecendo recomendações de filmes e séries. Isso não apenas aprimora a experiência do usuário, mas também impulsiona a fidelidade à plataforma."

  return (
    <div className={styles.container}>
        <div style={{ width: '100%', height: '100%'}}>
            <Image
              objectFit="cover"
              src={blockMoldure2Img}
              alt="block moldure image"
              style={{ position: 'relative',width: '80%', height: '80%', marginTop:'11vh', marginBottom:'11.2vh', left:'4vw' }}
            />
            <div style={{ maxWidth:'600px'}}>
                <h1 className={styles.textContainerConfig}>
                {text5}
                </h1>
            </div>
        </div>
        <div className={styles.textContainer}>
            <h2 className={styles.textConfig}>
                {text}
            </h2>
            <h2 className={styles.textConfig2}>
                {text2}<br />
                <br />{text3}
            </h2>
            <h2 className={styles.textConfig}>
                {text4}
            </h2>
        </div>
    </div>
  );
};

export default MyComponent;
