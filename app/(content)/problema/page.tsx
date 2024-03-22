import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { moldure, title, arrow } from './problema-images'
import { pixterDisplay } from '@/fonts';

export default function ProblemaIndexPage() {
  return (
    <div className={`${pixterDisplay.className} flex flex-col justify-center items-center`}>
      <div className='max-h-fit max-w-fit'>
        <div className='size-full'>
          <Image
            src={moldure}
            alt="page moldure"
            objectFit="cover"
          />
        </div>
        <div className='size-full absolute top-0 z-10'>
          <p className='text-[#83F0FF] text-[3vw] relative top-4 left-10'>
            {'//: A PROBLEMÁTICA DA IA'}
          </p>
          <div className='flex relative left-10 md:left-[20%] top-28 w-full gap-[5%]'>
            <div className='relative h-[25vw] flex'>
              <Image
                src={title}
                alt="page title"
                style={{ width: '100%', height: '100%' }}
              />
            </div>
            <p className='text-[#83F0FF] text-[1.2vw] mt-[10%]'>
              {'//:TÓPICOS'}
            </p>
            <div className='-mt-10 w-[45%] sm:w-60 lg:w-[20%] sm:mt-[10%]'>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
              <Link href="/problema/conhecimento">
                <Button variant="ghost" className='p-0 m-0 w-full flex justify-start py-10'>
                  <p className='text-[#83F0FF] text-[1vw]'>
                    {'//:001'}
                  </p>
                  <p className='ml-[15%] mr-auto font-sans'>
                    Você conhece alguma IA?
                  </p>
                  <Image
                    src={arrow}
                    alt="Seta"
                    width={20}
                    height={20}
                  />
                </Button>
              </Link>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
              <Link href="/problema/dia-a-dia">
                <Button variant="ghost" className='p-0 m-0 w-full flex justify-start py-10'>
                  <p className='text-[#83F0FF] text-[1vw]'>
                    {'//:002'}
                  </p>
                  <p className='ml-[15%] mr-auto font-sans'>
                    IA no dia a dia
                  </p>
                  <Image
                    src={arrow}
                    alt="Seta"
                    width={20}
                    height={20}
                  />
                </Button>
              </Link>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

