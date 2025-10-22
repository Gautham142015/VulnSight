import { render, screen } from '@testing-library/react';
import App from './App';

test('renders VulnSight header', () => {
  render(<App />);
  const linkElement = screen.getByText(/VulnSight/i);
  expect(linkElement).toBeInTheDocument();
});
