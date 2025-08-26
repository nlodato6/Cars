import Container from 'react-bootstrap/Container';
import { Navbar, Nav } from 'react-bootstrap';
import logo from '../assets/react.svg';

function Navbar2() {
  return (
    <Navbar sticky='top' expand='lg' bg="dark" className="bg-blue-400" data-bs-theme="dark">
      <Container>
        <Navbar.Brand className='text-white' href="/">
          <img
            alt="Logo"
            src={logo}
            width="50"
            height="50"
            className="d-inline-block align-middle mr-4"
          /> Cars Api
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto my-2 my-lg-0">
            <Nav.Link className='text-white' href="/ads">Ads</Nav.Link>
            <Nav.Link className='text-white' href="/cars">Cars</Nav.Link>
            <Nav.Link className='text-white' href="/models">Models</Nav.Link>
            <Nav.Link className='text-white' href="/users">Users</Nav.Link>
            <Nav.Link className='text-white' href="/profiles">User Profiles</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navbar2;