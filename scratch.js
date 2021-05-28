const express = require('express')
var bodyParser = require('body-parser')

const app = express()
const port = 3000
app.use(bodyParser.json())

app.get('/', (req, res) => {
  let data = req.body.data
  let id =data.id
  let image_url = data.image_url

  
  
  res.send(id)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
}) 

