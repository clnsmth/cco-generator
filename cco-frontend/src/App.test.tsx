import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from './App';
import '@testing-library/jest-dom'; // enhances expect()

describe('Frontend Sanity Check', () => {
    it('renders the main application wrapper', () => {
        render(<App />);
        const mainElement = screen.getByRole('main') || document.body;
        expect(mainElement).toBeTruthy();
    });
});
