import React from 'react'
import {motion} from 'framer-motion'

export default function Box3() {

    const boxVariant = {
        lion: {
            x:100,
            scale: 1.5,
            backgroundColor: "blue"
        },
        elephant:{
            x: 1000,
            scale : 0.3,
            backgroundColor: "green"
        }
    }

  return (
  <div className = 'box-container'>
      <motion.div className='box'
      variants={boxVariant}
      initial= "lion"
      animate = "elephant"
      >

      </motion.div>

      
    </div>
  )
}
