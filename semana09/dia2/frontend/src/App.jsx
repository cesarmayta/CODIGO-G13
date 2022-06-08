import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container,Row,Col,Card,Button,Table,Form} from 'react-bootstrap';


function App() {
  const [count, setCount] = useState(0)

  return (
    <section className="vh-100">
        <Container className="container py-5 h-100">
          <Row className="row d-flex justify-content-center align-items-center h-100">
            <Col className="col col-lg-9 col-xl-7">
              <Card className="card rounded-3">
                <Card.Body className="card-body p-4">
      
                  <h4 className="text-center my-3 pb-3">Lista de Tareas</h4>
      
                  
                    <Col className="col-12">
                      <div className="form-outline">
                        <input type="text" id="form1" className="form-control" />
                      </div>
                    </Col>
      
                    <div className="col-12">
                      <button type="submit" className="btn btn-primary">Agregar Tarea</button>
                    </div>
      
                  <Table className="table mb-4">
                    <thead>
                      <tr>
                        <th scope="col">No.</th>
                        <th scope="col">Tarea</th>
                        <th scope="col">Acciones</th>
                      </tr>
                    </thead>
                    <tbody id="cuerpoTabla">
                    </tbody>
                  </Table>
      
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </section>
  )
}

export default App
