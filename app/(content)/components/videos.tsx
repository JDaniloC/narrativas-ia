"use client";

import { Carousel } from "react-responsive-carousel";

export default function VideoSlide() {
  return (
    <Carousel
      showArrows={true}
      infiniteLoop={true}
      showIndicators={true}
      dynamicHeight={false}
      showThumbs={false}
    >
      <div>
        <video controls style={{ width: '100%', height: '100%' }}>
          <source src="/your_name_en_dub.mp4" />
        </video>
        <p className="legend !bottom-16">Your Name | Play HT</p>
      </div>
      <div>
        <video controls style={{ width: '100%', height: '100%' }}>
          <source src="/tsurezure_children.mp4" />
        </video>
        <p className="legend !bottom-16">Tsurezure Children</p>
      </div>
      <div>
        <video controls style={{ width: '100%', height: '100%' }}>
          <source src="/your_name_br_dub.mp4" />
        </video>
        <p className="legend !bottom-16">Your Name | ElevenLabs (BR)</p>
      </div>
      <div>
        <video controls style={{ width: '100%', height: '100%' }}>
          <source src="/your_name_elevenlabs.mp4" />
        </video>
        <p className="legend !bottom-16">Your Name | ElevenLabs (EN)</p>
      </div>
      <div>
        <video controls style={{ width: '100%', height: '100%' }}>
          <source src="/your_name_runway.mp4" />
        </video>
        <p className="legend !bottom-16">Your Name | Runway</p>
      </div>
    </Carousel>
  )
}